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
    
    pattern = r'^([\d,]+|[가-힣]+)$'
    if not re.match(pattern, s):
        return None

    if ',' in s:
        parts = s.split(',')
        for p in parts:
            if not p.isdigit():
                return None
        
        total_len = len(s.replace(',', ''))
        if total_len == 0:
            return None
            
        # Check comma positioning (standard 3-digit grouping)
        temp_s = s.replace(',', '')
        if not temp_s.isdigit():
            return None
            
        # Validate comma placement logic
        # A valid comma-separated number like 1,234 or 1,234,567
        # The digits between commas must be exactly 3, except for the first group
        parts = s.split(',')
        if len(parts) > 1:
            if len(parts[0]) == 0 or any(len(p) != 3 for p in parts[1:]):
                return None
            if len(parts[0]) > 3:
                return None
        else:
            # If no comma, it's just a pure digit string
            pass

        # Re-verify if the string is strictly numeric after removing commas
        if not s.replace(',', '').isdigit():
            return None
        
        # If there are units mixed with commas, it's invalid per rule "단위 표현은 ','와 같이 쓰일 수 없다"
        # But wait, the prompt says "단위 표현은 ','와 같이 쓰일 수 없다." 
        # This implies if a unit exists, no comma can exist in the whole string.
        # Let's check if any unit exists in the original string
        for u in units:
            if u in s:
                return None

    # Handle cases with units
    has_unit = False
    for u in units:
        if u in s:
            has_unit = True
            break
    
    if has_unit:
        # Rule: "단위 표현은 ','와 같이 쓰일 수 없다."
        if ',' in s:
            return None
            
        # Split by units and process
        # Example: "123만4567억" -> This is tricky. Usually it's "1억2345만..."
        # We need to parse from largest unit to smallest
        
        total_value = 0
        current_num_str = ""
        
        # Regex to find numbers and units
        # Matches groups like (123)(만) or (4567)(억)
        tokens = re.findall(r'(\d+)([가-힣]+)', s)
        
        # Check if the sum of tokens covers the whole string (excluding digits/units)
        # This is complex, let's use a simpler approach:
        # Find all segments of [digits][unit]
        
        # First, check if the string contains invalid characters
        if re.search(r'[^\d가-힣]', s):
            return None

        # Reconstruct the value
        # We split the string into parts of (digits)(unit)
        # But '만' can have 1-4 digits before it.
        
        # Correct approach for Korean numbering:
        # Iterate through units from largest to smallest
        remaining_s = s
        total_val = 0
        
        # We need to find the position of each unit
        # Since units are hierarchical, we can find them in order
        found_units = []
        for u in ['조', '억', '만', '천']:
            idx = remaining_s.find(u)
            if idx != -1:
                found_units.append((u, idx))
        
        # Sort units by their appearance in the string (highest value first usually)
        # Actually, the string is parsed left to right.
        # "1조2000억" -> 1 is at index 0, 2000 is at index 4.
        
        # Let's use a regex to find all [number][unit] pairs
        # and also check if there's a leading number without a unit
        # e.g., "1234만" -> 1234 is the number for 만
        # "1억2345만" -> 1 is for 억, 2345 is for 만
        
        parts = re.split(r'([가-힣]+)', s)
        # parts will look like ['1', '억', '2345', '만', '']
        
        current_val = 0
        for i in range(0, len(parts)-1, 2):
            num_part = parts[i]
            unit_part = parts[i+1]
            
            if not num_part.isdigit():
                return None
            
            val = int(num_part)
            multiplier = 0
            if unit_part == '조': multiplier = 10**12
            elif unit_part == '억': multiplier = 10**8
            elif unit_part == '만': multiplier = 10**4
            elif unit_part == '천': multiplier = 10**3
            else: return None # Should not happen due to regex
            
            current_val += val * multiplier
            
        # Check if there is a trailing number without a unit (e.g., "1억23")
        # In Korean "1억23" means 100,000,023? No, usually it's "1억 23원"
        # If the last part is a digit, it's the base unit (ones).
        last_idx = len(parts) - 1
        if len(parts) % 2 == 1 and parts[-1].isdigit() and parts[-1] != '':
            # This handles cases like "1억23"