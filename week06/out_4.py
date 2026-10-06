import re

def parse_won(s):
    if not s:
        return None

    s = s.strip()
    if s.endswith('원'):
        s = s[:-1]
    
    if not s:
        return None

    units = ['조', '억', '만', '천']
    unit_map = {'조': 10**12, '억': 10**8, '만': 10**4, '천': 10**3}
    
    if re.search(r'[,]\s*[가-힣]', s) or re.search(r'[가-힣]\s*[,]', s):
        return None

    if ',' in s:
        parts = s.split(',')
        for i, part in enumerate(parts):
            if not part.isdigit():
                return None
            if i == 0:
                if len(part) != 3 and len(part) != 1:
                    if len(part) == 4 and part != '0': # exception for leading zeros logic
                        pass 
            else:
                if len(part) != 3:
                    return None
        
        check_s = s.replace(',', '')
        if re.search(r'[가-힣]', check_s):
            return None
        
        try:
            val = int(check_s)
            return str(val)
        except ValueError:
            return None

    pattern = r'^(\d+[가-힣]?)+$'
    if not re.match(pattern, s):
        return None

    total = 0
    temp_num = ""
    
    i = 0
    while i < len(s):
        if s[i].isdigit():
            temp_num += s[i]
            i += 1
        else:
            unit_char = s[i]
            if unit_char not in unit_map:
                return None
            
            if not temp_num:
                return None
            
            val = int(temp_num)
            if val == 0:
                pass
            
            # Check if unit is valid (e.g., 1234만 is okay, but 12345만 is not per logic of "1~4 digits")
            if len(temp_num) > 4:
                return None
                
            total += val * unit_map[unit_char]
            temp_num = ""
            i += 1
            
            # After a unit, we can only have a larger unit or end
            # But the rule says units are 만, 억, 조. 천 is usually handled by digits.
            # If '천' is used as a unit like '1천', it's treated here.
            
    if temp_num:
        if len(temp_num) > 4:
            return None
        total += int(temp_num)

    # Final validation: Reconstruct string to see if it matches input logic
    # This is complex, so we use a simpler approach: parse segments.
    
    # Alternative Parsing Logic for Units
    segments = []
    current_num = ""
    for char in s:
        if char.isdigit():
            current_num += char
        else:
            if not current_num: return None
            segments.append((int(current_num), char))
            current_num = ""
    if current_num:
        segments.append((int(current_num), ""))

    # Validate segments order and digit counts
    res = 0
    last_unit_val = 0
    for val, unit in segments:
        u_val = unit_map.get(unit, 1)
        if unit != "" and unit != '천': # '천' is tricky, usually part of digits
             if u_val <= last_unit_val: return None
             if len(str(val)) > 4: return None
        
        if unit == '천':
            # If '천' is explicitly written, treat it as 1000
            if val > 9: return None # e.g., 12천 is invalid, should be 1만 2천
            res += val * 1000
            last_unit_val = 1000
        elif unit == "":
            res += val
            last_unit_val = 1
        else:
            if u_val <= last_unit_val: return None
            res += val * u_val
            last_unit_val = u_val

    # To ensure "1~4 digits before unit" and "correctness"
    # Let's use a more robust regex-based segmenter
    
    final_total = 0
    unit_list = [('조', 10**12), ('억', 10**8), ('만', 10**4), ('천', 10**3)]
    
    # Find all units in string
    found_units = []
    for u_name, u_val in unit_list:
        idx = s.find(u_name)
        if idx != -1:
            found_units.append((idx, u_name, u_val))
    
    found_units.sort()
    
    # Check if units are in descending order
    for j in range(len(found_units)-1):
        if found_units[j][2] <= found_units[j+1][2]:
            return None

    # Extract numbers
    parts = []
    last_idx = 0
    for idx, u_name, u_val in found_units:
        num_part = s[last_idx:idx]
        if not num_part: return None
        if not num_part.isdigit(): return None
        if len(num_part) > 4: return None
        parts.append((int(num_part), u_val))
        last_idx = idx + 1
    
    remaining = s[last_idx:]
    if remaining:
        if not remaining.isdigit(): return None
        if len(remaining) > 4: return None
        parts.append((int(remaining), 1))
    
    # Re-verify the whole string structure
    # The sum of parts must represent the original logic
    actual_sum = 0
    for v, uv in parts:
        actual_sum += v * uv
        
    # One more check: does the