import re

def parse_won(s):
    if not s:
        return None

    s = s.strip()
    if s.endswith('원'):
        s = s[:-1].strip()
    
    if not s:
        return None

    units = ['만', '억', '조', '경']
    unit_map = {u: 10**(4 * (i + 1)) for i, u in enumerate(units)}
    
    if re.search(r'[가-힣]{2,}', s):
        return None

    if re.search(r'[,가-힣]', s):
        parts = re.split(r'[,가-힣]', s)
        for p in parts:
            if not p: continue
            if not re.fullmatch(r'\d+', p):
                return None

    if ',' in s:
        temp = s.replace(',', '')
        if not re.fullmatch(r'\d+', temp):
            return None
        
        original_parts = s.split(',')
        if len(original_parts) > 1:
            for i in range(len(original_parts) - 1):
                if not re.fullmatch(r'\d+', original_parts[i]):
                    return None
            last_part = original_parts[-1]
            if not re.fullmatch(r'\d+', last_part):
                return None
            if len(last_part) > 3:
                return None
            if len(last_part) > 0 and last_part != '0' and not last_part.startswith('0'):
                pass 
            
            check_val = int(temp)
            if len(temp) > 1 and (len(temp) - 1) % 3 != 0:
                return None
        else:
            if not re.fullmatch(r'\d+', s.replace(',', '')):
                return None

    tokens = re.findall(r'\d+|[가-힣]', s)
    if not tokens:
        return None
    
    total_val = 0
    current_group_val = 0
    group_digit_count = 0
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        if token.isdigit():
            num = int(token)
            current_group_val += num
            group_digit_count += len(token)
            
            if i + 1 < len(tokens) and tokens[i+1] in unit_map:
                unit_name = tokens[i+1]
                if group_digit_count > 4:
                    return None
                total_val += current_group_val * unit_map[unit_name]
                current_group_val = 0
                group_digit_count = 0
                i += 2
            else:
                i += 1
        elif token in unit_map:
            if current_group_val == 0 and group_digit_count == 0:
                return None
            if group_digit_count > 4:
                return None
            total_val += current_group_val * unit_map[token]
            current_group_val = 0
            group_digit_count = 0
            i += 1
        else:
            return None

    total_val += current_group_val
    
    final_str = str(total_val)
    
    reconstructed = ""
    temp_val = total_val
    
    if temp_val == 0:
        return "0"

    parts = []
    
    rem = total_val
    for unit, multiplier in sorted(unit_map.items(), key=lambda x: x[1], reverse=True):
        if rem >= multiplier:
            sub = rem // multiplier
            if sub > 0:
                parts.append((sub, unit))
            rem %= multiplier
    if rem > 0:
        parts.append((rem, ""))

    # Validation of the logic against input string structure
    # Re-verifying if the input string matches the parsed integer's scale
    # The prompt asks to return the integer as a string.
    
    # Final check for comma rule via the parsed number
    s_no_comma = s.replace(',', '')
    if not s_no_comma.isdigit():
        # Check if it was mixed with units
        digits_only = ""
        for t in tokens:
            if t.isdigit(): digits_only += t
        if not digits_only: return None

    return str(total_val)