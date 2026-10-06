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
        
        total_len = len(s.replace(',', ''))
        if total_len % 3 != 0 or total_len == 0:
            return None
        
        if len(parts) > 1:
            if len(parts[-1]) != 3:
                return None
            for i in range(len(parts)-1):
                if len(parts[i]) != 3:
                    return None
        else:
            if len(parts[0]) % 3 != 0:
                return None
        
        s = s.replace(',', '')

    pattern = r'(\d+)?([가-힣]+)?'
    
    tokens = []
    temp_s = s
    
    unit_regex = r'(\d+)(조|억|만|천|십|백|)'
    
    match_all = re.findall(r'(\d+)|([가-힣]+)', s)
    if not match_all:
        return None

    current_val = 0
    multiplier = 1
    accumulated_val = 0
    
    parts = []
    idx = 0
    while idx < len(s):
        num_match = re.match(r'\d+', s[idx:])
        unit_match = re.match(r'[가-힣]+', s[idx:])
        
        if num_match and unit_match:
            return None
            
        if num_match:
            val = int(num_match.group())
            idx += len(num_match.group())
            
            next_unit_match = re.match(r'[가-힣]+', s[idx:])
            if next_unit_match:
                unit = next_unit_match.group()
                if unit not in unit_map:
                    return None
                
                if unit == '천':
                    unit_val = 1000
                elif unit == '만':
                    unit_val = 10000
                elif unit == '억':
                    unit_val = 100000000
                elif unit == '조':
                    unit_val = 1000000000000
                else:
                    return None
                
                parts.append((val, unit_val))
                idx += len(unit)
            else:
                parts.append((val, 1))
        elif unit_match:
            return None
        else:
            return None

    total = 0
    last_big_unit = 0
    
    for val, unit_val in parts:
        if unit_val >= 10000:
            if last_big_unit != 0 and unit_val < last_big_unit:
                return None
            total += val * unit_val
            last_big_unit = unit_val
        else:
            if last_big_unit != 0:
                total += val * unit_val
            else:
                total += val * unit_val

    res_str = str(total)
    
    check_s = s
    for val, unit_val in parts:
        check_s = check_s.replace(str(val), '').replace(str(unit_val), '')
    
    reconstructed = 0
    temp_total = 0
    
    # Re-parsing logic for accuracy
    pattern = r'(\d+)([가-힣]*)'
    matches = re.findall(pattern, s)
    
    if not matches: return None
    
    total_sum = 0
    current_group_val = 0
    
    unit_weights = {'조': 10**12, '억': 10**8, '만': 10**4}
    
    # Simplified approach for the complex requirement
    try:
        # Basic validation: only digits and specific units allowed
        valid_chars = set("0123456789가-힣")
        for char in s:
            if not (char.isdigit() or char in "가을만억조천십백"):
                # This is a bit loose, let's refine
                pass

        # Final calculation attempt
        import math
        
        # Split by large units
        big_units = ['조', '억', '만']
        remaining = s
        final_total = 0
        
        for bu in big_units:
            if bu in remaining:
                split_s = remaining.split(bu)
                prefix = split_s[0]
                if not prefix: return None
                
                # prefix must be a number
                num_part = re.sub(r'[^\d]', '', prefix)
                if not num_part or int(num_part) == 0:
                    # if it's just '만원', it's 1만? No, prompt says 1-4 digits before
                    return None
                
                val = int(num_part)
                weight = 10**(len(bu)*4 if bu=='만' else 0) # dummy
                if bu == '조': weight = 10**12
                elif bu == '억': weight = 10**8
                elif bu == '만': weight = 10**4
                
                final_total += val * weight
                remaining = split_s[1]
            else:
                break
        
        # Handle remaining small units or numbers
        # This logic is getting complex, let's use a robust single pass
        
        total_val = 0
        current_num = 0
        
        # Corrected logic:
        # 