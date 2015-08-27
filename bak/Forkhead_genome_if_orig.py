

def find_forkhead(chrom_ident, pattern):
    from intermine.webservice import Service
    service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

    # Get a new query on the class (table) you will be querying:
    query = service.new_query("Chromosome")

    # The view specifies the output columns
    query.add_view("primaryIdentifier", "sequence.residues")

    # Uncomment and edit the line below (the default) to select a custom sort order:
    # query.add_sort_order("Chromosome.primaryIdentifier", "ASC")
    #chrIII = 'GATTACAGGGAATTTGTTTAATAGCAATTTATACGCTTTGTTATCGGCACCACCAAATTCTGGGATAACCGTTAATTCTTCCTCAGGTTTGCCTAGTGGATCCTCTCCTTCTGGAGTTTGGCCACGCTCTGGCTTTTCGATCAGACTTGGCATGTGACTAATCAAGTATGGCATGCTGGTTTTTGGGTCCTTTGTTTTCGTTGTTTCAGTCTGGATAAATTTTAAGTTACCATTATCGAAGGCACTTTTGTACTTGTCACTAATTAAAGATGCAATGTCAGCGGGGATACTCATTTTTATTTTAATTTTTACTTTTCTGTTTGTTCTAAAATCTATCTAAACTGGCTTTCAAGATCAATCTATTGTCTTTTAAGGTAAACTTTAAATTGGAAATAATAGTAATGTTAGTTCCTTCATTTTAACCTTGTATTGTATTTCCTTTGCGTGATGAAAAAAAAACTGAAAAAGAGAAAAATAAGAAAATCTTCTAGAACGTTCCGAAACAGGACACTTAGCACACAAATACAGAATAGGAAAGTAAAAGGCAATATATGAATGCAGTGCTTGTAACTGGTGCTTGTATCCAAGAATAGCTTCTTGCTGTAGGTTATGGGAATATCGTGTAAGCTGGGGTGACTTTTGAGCTATTCGCGACGCCCGACGCCGTAATAACTACTTTCGACAGACCACTTATGACAGTATTTCAGGCCGCTCTTATAAAATGACATGTTAACAAACAGTTCTGATTATTCGCCTTTTGACAGGACGATAATGTAAATAGTTGTGGTAGTATCATTCAGGTATGTAACTGTTTACTTTGTATCGCTTGAAAAAAATAAGCATTTCAGAGCCTTCTTTGGAGCTCAAGTGGATTGAGGCCACAGCAAGACCGGCCAGTTTGAATGCTCAACTCTTCAAAAGAAATTCCTCAAATATGTCCAGTTTCATGTACTGTCCGGTGTGATTTATTATTTTTTATTTACTTTGTAGTTCTTAAAGCTAAGATTTTTTTCTTTGATAAATTCTTGTTTTCATATCCTAAAATTAAAGGGAAAATAAACAATACATAACAAAACATATAAAAACCAACACAATAAAAAAAAGGATCAAATACTCATTAAAGTAACTTACACGGGGGCTAAAAACGGAGTTTGATGAATATTCACAAGATAAAAATCATATGTATGTTTCTGATATATCGATATACAATCAAACACTTTCAAGAATTTGTTTGTAGACTTTTTGCTAGAGACCTCATCAAAGTGCTACCAACTAAGATCAACTTATACTTCTTTTAGAGAAAATTTTTTTCAATGTACTCCAAAGAGATTTAGATCCTGTCTCTTCCTCTTCCTCTTCCTCGAAAGTCAAAGAAAAATCAGAGTCTCCCTGCTTATTCAGGCGGAGAGGCTCTAGGGTAGTTGCGTTTCTCTCATTGGGACACTGAACCTCATTTTCCAACATTTTGGTCATGTAAGAGGCGACAGGCTCATCGCAGGTGGGTGCATCAACATGGTAGTACCTGGACCAAGCGCTACATTGAGTCCCTCCTGGATAAACACCGCTACAATATTGTCTTTGGACGTTTGCCCAAACCATATCTTTTGAATACCAAAGCTGGACCACATTGTATGGCCTAATCATTGGTGCTACCATAATACTGGATTGGGAAACAGTCTGGTTAATTTTTTTCAACCAATTTTTCTTATCTAGCAATGATTTAATAAACCTGAAATCTAAATTGTCTTCGTTAGCGTCTGTGTCATAATCTACAATTGAGTACTGTGACGTCCAATTATATGGCACCGAGATGGGGAATCTGTCCGGTGTTTCGTCGCTGTTATCCTTCTCCTCCCTCCAAATGCAGTCAGAGGCAGGTGCCCATTCGGTTCGCCAGTCTCCGTTATTTACTACTTGGTACTGTTCCCAATCGTAATACGTTTCCTCTGGGTTGAAGATACTTGCTCTGCTCTTGACATTGCCCATAGCCACACCACGAGAAACATCGTGGAAGATTACGGAGCTGTTTACGATAGCAGGAGCAATGGATTTGACGAATGACACTTGATAAAAGTCTTTGGTCGAAAA'

    chromosome = ''
    for row in query.rows():
        if row["primaryIdentifier"] == chrom_ident:
            chromosome = row["sequence.residues"]

    def rev_comp(dna):
        comp = ''
        for nucl in dna:
            if nucl == 'A':
                comp = comp + 'T'
            elif nucl == 'T':
                comp = comp + 'A'
            elif nucl == 'C':
                comp = comp + 'G'
            elif nucl == 'G':
                comp = comp + 'C'
            else:
                print 'Not a DNA sequence'

        rev_comp = comp[::-1]
        return rev_comp

    chromosome_rev = rev_comp(chromosome)



    #seq = 'AAACAGGACACTTAGCACACAAATACAGAATAGGAAAGTAAAAGGCAATATATGAATGCAGTGCTTGTAACTGGTGCTTGTATCCAAGAATAGCTTCTTGCTGTAGGTTATGGGAATATCGTGTAAGCTGGGGTGACTTTTGAGCTATTCGCGACGCCCGACGCCGTAATAACTACTTTCGACAGACCACTTATGACAGTATTTCAGGCCGCTCTTATAAAATGACATGTTAACAAACAGTTCTGATTATTCGCCTTTTGACAGGACGATAATGTAAATAGTTGTGGTAGTATCATTCAGGTATGTAACTGTTTACTTTGTATCGCTTGAAAAAAATAAGCATTTCAGAGCCTTCTTTGGAGCTCAAGTGGATTGAGGCCACAGCAAGACCGGCCAGTTTGAATGCTCAACTCTTCAAAAGAAATTCCTCAAATATGTCCAGTTTCATGTACTGTCCGGTGTGATTTATTATTTTTTATTTACTTTGTAGTTCTTAAAGCTAAGATTTTTTTCTTTGATAAATTCTTGTTTTCATATCCTAAAATTAAAGGGAAAATAAACAATACATAACAAAACATATAAAAACCAACACAATAAAAAAAAGGATCAAATACTCATTAAAGTAACTTACACGGGGGCTAAAAACGGAGTTTGATGAATATTCACAAGATAAAAATCATATGTATGTTTCTGATATATCGATATACAATCAAACACTTTCAAGAATTTGTTTGTAGACTTTTTGCTAGAGACCTCATCAAAGTGCTACCAACTAAGATCAACTTATACTTCTTTTAGAGAAAATTTTTTTCAATGTACTCCAAAGAGATTTAGATCCTGTCTCTTCCTCTTCCTCTTCCTCGAAAGTCAAAGAAAAATCAGAGTCTCCCTGCTTATTCAGGCGGAGAGGCTCTAGGGTAGTTGCGTTTCTCTCATTGGGACACTGAACCTCATTTTCCAACATTTTGGTCATGTAAGAGGCGACAGGCTCATCGCAGGTGGGTGCATCAACATGGTAGTACCTGGACCAAGCGCTACATTGAGTCCCTCCTGGATAAACACCGCTACAATATTGTCTTTGGACGTTT'
    #seq_rev = rev_comp(seq)
    watson_finds = []
    crick_finds = []

    def find_pattern(pattern,seq):
        import regex
        find = regex.findall(pattern, seq)
        return find



    watson_finds =  find_pattern(pattern, chromosome)
    crick_finds = find_pattern(pattern, chromosome_rev)
    #WWWWTTTAYRTTTWGTT
    #acs = '([ATC][ATC][AT][AT]TTTA[TC][AG]TTT[AT]GTT){e<=1}'
    acs = '(AAC[TA]AAA[CT][GA]TAAA[AT][AT][GAT][GAT]){e<=1}'
    #acs = 'TTATATGTTTT'
    #acs = 'AAAACATATAA'
    import regex
    potential_origins = []

    for a in watson_finds:
        filtered_watson = []
        a = str(a)
        filtered_watson = regex.findall(acs, a)
        if len(filtered_watson) > 0:
            potential_origins.append(str(a))

    for a in crick_finds:
        filtered_crick = []
        a = str(a)
        filtered_crick = regex.findall(acs, a)
        if len(filtered_crick) > 0:
            potential_origins.append(a)

    print potential_origins

    motif_start_pos = []
    motif_end_pos = []
    motif_seq = []
    def find_motif(motif,seq):
        for a in range(0, len(seq)):
            slice = seq[a:a+len(motif)]
            if slice == motif:
                motif_start_pos.append(a+1) #+1 because first nuc is 1 not 0
                motif_end_pos.append((a+1) + len(motif))
                motif_seq.append(seq[a:a+len(motif)])

    for a in potential_origins:
        find_motif(a,chromosome)

    for a in potential_origins:
        a = rev_comp(a)
        find_motif(a,chromosome)

    count = 0
    f1 = open('Out_table_1.txt', 'a')
    for a in range(0, len(motif_start_pos)):
        f1.write(chrom_ident)
        f1.write(' ')
        motif_midpoint = (motif_start_pos[a] + motif_end_pos[a]) / 2
        f1.write(str(motif_midpoint))
        f1.write(' ')
        f1.write(str(motif_seq[a]))
        f1.write('\n')

#TRTTTAY
pattern1 = '(.{25}T[AG]TTTA[CT].{72}[AG]TAAA[CT]A){e<=2}'
pattern2 = '(.{25}T[AG]TTTA[CT].{72}T[AG]TTTA[CT]){e<=2}'
pattern3 = '(.{25}[AG]TAAA[CT]A.{72}T[AG]TTTA[CT]){e<=2}'
pattern4 = '(.{25}[AG]TAAA[CT]A.{72}[AG]TAAA[CT]A){e<=2}'


find_forkhead('chrI', pattern4)
find_forkhead('chrII', pattern4)
find_forkhead('chrIII', pattern4)
find_forkhead('chrIV', pattern4)
find_forkhead('chrV', pattern4)
find_forkhead('chrVI', pattern4)
find_forkhead('chrVII', pattern4)
find_forkhead('chrVIII', pattern4)
find_forkhead('chrIX', pattern4)
find_forkhead('chrX', pattern4)
find_forkhead('chrXI', pattern4)
find_forkhead('chrXII', pattern4)
find_forkhead('chrXII', pattern4)
find_forkhead('chrXIII', pattern4)
find_forkhead('chrXIV', pattern4)
find_forkhead('chrXV', pattern4)
find_forkhead('chrXVI', pattern4)
