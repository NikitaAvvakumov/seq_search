#!/usr/bin/env python

# This is an automatically generated script to run your query
# to use it you will require the intermine python client.
# To install the client, run the following command from a terminal:
#
#     sudo easy_install intermine
#
# For further documentation you can visit:
#     http://intermine.readthedocs.org/en/latest/web-services/

# The following two lines will be needed in every python script:
from intermine.webservice import Service
service = Service("http://yeastmine.yeastgenome.org/yeastmine/service")

# Get a new query on the class (table) you will be querying:
query = service.new_query("ARS")

# The view specifies the output columns
query.add_view(
    "chromosome.primaryIdentifier", "chromosomeLocation.start",
    "chromosomeLocation.end", "secondaryIdentifier"
)

# Uncomment and edit the line below (the default) to select a custom sort order:
# query.add_sort_order("ARS.chromosome.primaryIdentifier", "ASC")
'''
for row in query.rows():
    print row["chromosome.primaryIdentifier"], row["chromosomeLocation.start"], \
        row["chromosomeLocation.end"], row["secondaryIdentifier"]
'''
chromosome_list = []
average_list = []
identifier_list = []
for row in query.rows():
    chromosome_list.append(str(row["chromosome.primaryIdentifier"]))
    average = (float(row["chromosomeLocation.start"]) + float(row["chromosomeLocation.end"])) / 2
    average_list.append(average)
    identifier_list.append(str(row["secondaryIdentifier"]))

print chromosome_list
print average_list
print identifier_list


try:
    f = open('Pattern1_all_finds.txt')
except IOError:
    print 'File not found'

f1 = open('Overlap_table.txt', 'a')

margin = 100
count_overlaps = 0
count_motifs = 0
for a in f:
    count_motifs +=1
    rowlist = []
    a = str(a)
    rowlist = a.split()
    chr_ident = rowlist[0]
    motif_midpoint = float(rowlist[1])
    motif_seq = rowlist[2]

    for a in range(0,len(chromosome_list)):
        if chr_ident == chromosome_list[a]:
            if motif_midpoint > (average_list[a] - margin) and motif_midpoint < (average_list[a] + margin):
                count_overlaps += 1
                print chr_ident, motif_midpoint, average_list[a], motif_seq
                f1.write(str(chr_ident))
                f1.write(' ')
                f1.write(str(identifier_list[a]))
                f1.write(' ')
                f1.write(str(motif_midpoint))
                f1.write(' ')
                f1.write(str(average_list[a]))
                f1.write(' ')
                f1.write(str(motif_seq))
                f1.write('\n')

print count_motifs, count_overlaps, (float(count_overlaps)/float(count_motifs))*100
