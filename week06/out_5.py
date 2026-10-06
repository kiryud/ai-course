import re

def parse_won(s):
    if not s:
        return None

    s = s.strip()
    if s.endswith('원'):
        s = s[:-1].strip()
    
    if not s:
        return None

    units = ['조', '억', '만', '천']
    unit_map = {'조': 10**12, '억': 10**8, '만': 10**4, '천': 10**3}
    
    if re.search(r'[가-힣]{2,}', s):
        return None

    if ',' in s:
        parts = s.split(',')
        for p in parts:
            if not p.isdigit():
                return None
        
        total_str = "".join(parts)
        if len(total_str) % 3 != 0 or (len(total_str) % 3 != 0 and len(total_str) > 0):
            # This logic is slightly complex due to the requirement of "exact thousand separator"
            # Standard rule: from right, groups of 3.
            pass 
        
        # Re-verify comma placement
        temp_s = s.replace(',', '')
        check_s = ""
        for i, char in enumerate(reversed(temp_s)):
            if i > 0 and i % 3 == 0:
                check_s = "," + check_s
            check_s = char + check_s
        
        if check_s != s:
            return None
        
        s = temp_s

    pattern = r'^(\d+)?([가-힣]+)?$'
    
    def solve(text):
        res = 0
        current_val = 0
        
        i = 0
        while i < len(text):
            match = re.match(r'(\d+)([가-힣]+)', text[i:])
            if match:
                num_part = match.group(1)
                unit_part = match.group(2)
                
                if len(unit_part) > 1:
                    if unit_part == '만' or unit_part == '억' or unit_part == '조':
                        pass
                    else:
                        return None
                
                val = int(num_part)
                u_idx = units.index(unit_part)
                multiplier = unit_map[unit_part]
                
                # Check if unit is valid (only single characters allowed for specific units)
                if len(unit_part) > 1: return None
                
                res += val * multiplier
                i += len(num_part) + len(unit_part)
            elif text[i:].isdigit():
                res += int(text[i:])
                break
            else:
                return None
        return res

    # Refined approach for Korean numbering
    total_num = 0
    temp_s = s
    
    # Check if it contains only digits and valid units
    valid_chars = set("0123456789만억조천")
    for char in temp_s:
        if char not in valid_chars:
            return None

    # Split by units
    parts = []
    curr = ""
    for char in temp_s:
        if char in "만억조":
            if not curr: return None
            parts.append((int(curr), char))
            curr = ""
        else:
            curr += char
    if curr:
        if any(u in curr for u in "만억조"): return None
        parts.append((int(curr), None))
    elif not parts:
        return None

    # Calculate
    try:
        ans = 0
        last_unit_val = 0
        for val, unit in parts:
            if unit is None:
                ans += val
            else:
                u_val = unit_map[unit]
                # If multiple units, they must be hierarchical
                # e.g., 1억 2천 -> 1*10^8 + 2*10^3
                ans += val * u_val
        
        # Final validation: check if the original string can be reconstructed or is logically sound
        # The problem asks to return a string of integers.
        return str(ans)
    except:
        return None

# The above logic is complex. Let's provide a cleaner version following all rules strictly.

def parse_won(s):
    if not s: return None
    s = s.strip()
    if s.endswith('원'): s = s[:-1].strip()
    if not s: return None

    # Comma validation
    if ',' in s:
        parts = s.split(',')
        if not all(p.isdigit() for p in parts): return None
        combined = "".join(parts)
        # Validate comma positions from right
        rev_comb = combined[::-1]
        valid_comma = True
        comma_count = 0
        for i in range(len(combined)):
            if (len(combined) - 1 - i) > 0 and (len(combined) - 1 - i) % 3 == 0:
                if s[len(s)-1-i] != ',': # This part is tricky
                    pass
        # Simpler comma check
        check_s = ""
        for i, digit in enumerate(reversed(combined)):
            if i > 0 and i % 3 == 0:
                check_s = "," + check_s
            check_s = digit + check_s
        if check_s != s: return None
        s = combined

    # Unit parsing
    units = [('조', 10**12), ('억', 10**8), ('만', 10**4), ('천', 10**3)]
    total = 0
    remaining = s
    
    # Check for invalid characters
    allowed = set("0123456789만억조천")
    if not all(c in allowed for c in s): return None

    # Extract numbers and units
    # Regex to find (number)(unit) or just (number)
    # Since we validated chars, we can use regex on the cleaned string
    import re
    matches = re.findall(r'(\d+)([가-힣])?', s)
    
    # If there are no matches or something