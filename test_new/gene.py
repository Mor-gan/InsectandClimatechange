def parse_blast_result(output1_7):
    with open(output1_7, 'r') as blast_file:
        lines = blast_file.readlines()
    
    # Skip the header lines (if any)
    for i, line in enumerate(lines):
        if line.startswith('#'):
            continue
        else:
            break
    
    


