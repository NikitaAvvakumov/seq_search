def find_forkhead(chrom_ident, pattern):
    from intermine.webservice import Service
    service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

    # Get a new query on the class (table) you will be querying:
    query = service.new_query("Chromosome")

    # The view specifies the output columns
    query.add_view("primaryIdentifier", "sequence.residues")

    # Uncomment and edit the line below (the default) to select a custom sort order:
    # query.add_sort_order("Chromosome.primaryIdentifier", "ASC")

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
                print('Not a DNA sequence')

        rev_comp = comp[::-1]
        return rev_comp

    chromosome_rev = rev_comp(chromosome)

    watson_finds = []
    crick_finds = []

    def find_pattern(pattern,seq):
        import regex
        find = regex.findall(pattern, seq)
        return find

    watson_finds =  find_pattern(pattern, chromosome)
    crick_finds = find_pattern(pattern, chromosome_rev)
    #acs = '([ATC][ATC][AT][AT]TTTA[TC][AG]TTT[AT]GTT){e<=1}'
    acs = '(AAC[TA]AAA[CT][GA]TAAA[AT][AT][GAT][GAT]){e<=1}'
    #acs = 'TTATATGTTTT'
    #acs = 'AAAACATATAA'
    import regex
    all_matches = watson_finds + crick_finds

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

    for a in all_matches:
        find_motif(a,chromosome)

    for a in all_matches:
        a = rev_comp(a)
        find_motif(a,chromosome)

    count = 0

    with open('fkh_motifs.txt', 'a') as f:
        for a in range(0, len(motif_start_pos)):
            match_pattern = "Fkh pattern: {}\n".format(pattern)
            motif_midpoint = (motif_start_pos[a] + motif_end_pos[a]) / 2
            chrom_location = "{}, {}\n".format(chrom_ident, str(motif_midpoint))
            match_sequence = "{}\n\n".format(str(motif_seq[a]))
            f.write(match_pattern)
            f.write(chrom_location)
            f.write(match_sequence)

fkh_pattern_1 = '(.{25}T[AG]TTTA[CT].{72}[AG]TAAA[CT]A){e<=2}'
fkh_pattern_2 = '(.{25}T[AG]TTTA[CT].{72}T[AG]TTTA[CT]){e<=2}'
fkh_pattern_3 = '(.{25}[AG]TAAA[CT]A.{72}T[AG]TTTA[CT]){e<=2}'
fkh_pattern_4 = '(.{25}[AG]TAAA[CT]A.{72}[AG]TAAA[CT]A){e<=2}'
fkh_pattern_allan = '(.{25}[AG][CT][AC]AA[CT]A.{70,74}[AG][CT][AC]AA[CT]A)'

find_forkhead('chrI', fkh_pattern_4)
# find_forkhead('chrII', fkh_pattern_4)
# find_forkhead('chrIII', fkh_pattern_4)
# find_forkhead('chrIV', fkh_pattern_4)
# find_forkhead('chrV', fkh_pattern_4)
# find_forkhead('chrVI', fkh_pattern_4)
# find_forkhead('chrVII', fkh_pattern_4)
# find_forkhead('chrVIII', fkh_pattern_4)
# find_forkhead('chrIX', fkh_pattern_4)
# find_forkhead('chrX', fkh_pattern_4)
# find_forkhead('chrXI', fkh_pattern_4)
# find_forkhead('chrXII', fkh_pattern_4)
# find_forkhead('chrXII', fkh_pattern_4)
# find_forkhead('chrXIII', fkh_pattern_4)
# find_forkhead('chrXIV', fkh_pattern_4)
# find_forkhead('chrXV', fkh_pattern_4)
# find_forkhead('chrXVI', fkh_pattern_4)
#
# find_forkhead('chrI', fkh_pattern_allan)
# find_forkhead('chrII', fkh_pattern_allan)
# find_forkhead('chrIII', fkh_pattern_allan)
# find_forkhead('chrIV', fkh_pattern_allan)
# find_forkhead('chrV', fkh_pattern_allan)
# find_forkhead('chrVI', fkh_pattern_allan)
# find_forkhead('chrVII', fkh_pattern_allan)
# find_forkhead('chrVIII', fkh_pattern_allan)
# find_forkhead('chrIX', fkh_pattern_allan)
# find_forkhead('chrX', fkh_pattern_allan)
# find_forkhead('chrXI', fkh_pattern_allan)
# find_forkhead('chrXII', fkh_pattern_allan)
# find_forkhead('chrXII', fkh_pattern_allan)
# find_forkhead('chrXIII', fkh_pattern_allan)
# find_forkhead('chrXIV', fkh_pattern_allan)
# find_forkhead('chrXV', fkh_pattern_allan)
# find_forkhead('chrXVI', fkh_pattern_allan)
