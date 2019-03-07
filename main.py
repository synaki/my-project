 #Editor for inserting genes using transposon
#Finds the positions of the inserted transposon and the gene

# Imports
from Bio import SeqIO
from Bio.Seq import Seq
import random
import operator

#function to get input from the user
def usage(Sensor):
    #imports the essential transposon gene from the local directory
    for TnsA in SeqIO.parse("tnsA.txt", "fasta"):
        tnsA = TnsA.seq
    # transposes A which forms a complex with the transposes B and C to form a nick in the DNA
    for TnsB in SeqIO.parse("tnsB.txt", "fasta"):
        tnsB = TnsB.seq
    for TnsC in SeqIO.parse("tnsC.txt", "fasta"):
        tnsC = TnsC.seq
    for TnsD in SeqIO.parse("tnsD.txt", "fasta"):
        tnsD = TnsD.seq
    # transposes D which further helps in the choosing the desired position
    gene = tnsA + tnsB + tnsC + tnsD
    #concatinates the transposes to form a new sequence
    print("The insert tn7 transposes length is :", len(gene))
    #
    product = gene
    tn7_insert = Sensor[:1]+Sensor +tnsA +tnsB+tnsC+tnsD + Sensor[:1]
    print(tn7_insert)
    #
    print("The final insert and tn7 transposes length is :", len(tn7_insert))
    #
    for Tns5 in SeqIO.parse("tn5.txt", "fasta"):
        tns5 =Tns5.seq
    #
    print("The length of tn5 transposes is :", len(tns5))
    #
    tn5_insert = Sensor + tns5
    print(tn5_insert)
    print("The final insert and tn5 transposes length is :", len(tn5_insert))
    #
    return tn5_insert, tn7_insert
    #

#function which gets input from the user
def user_input():
    print("Input limited to fasta or genbank file")
    # Gives access to the user to import their genome of interest
    #regulating the input file formats
    try:
        input_genome = input("please insert the genome to be edited: ")

    except FileNotFoundError:

        print("%s cannot be opened for reading" % (input_genome))

    else:

        for sequence in SeqIO.parse(input_genome, "fasta"):
            input_data = sequence.seq
            print("The length of the given input genome sequence is ")
            print(len(input_data))

    #Imports sequence using biopython limited to fasta format

        for sequence in SeqIO.parse(input_genome, "gb"):

            print("The length of the given input genome sequence is ")

            print(len(sequence))
    #Imports sequence using biopython limited to genbank sequence

    insert_Gene = input("Please insert the desired gene of interest :")
    #gets the desired gene from the user
    for fragment in SeqIO.parse(insert_Gene, "fasta"):
        print("The length of the desired gene of interest")
        print(len(fragment.seq))
        Sensor = fragment.seq

    return Sensor, input_data

#predicts the location at which tn7 transposes insert the desired DNA
def location_predictor():
    try:
        location = float(input("Please provide the insert position using tn7: "))

    except:
        print("input is restricted to float")

    genome_map = int(46416.52 * location)
    print("The Insertion position is :", genome_map)
    return genome_map

#function helps to insert the transposon carring segment at desired location
def tn7(genome_map, input_data, Sensor, tn7_insert):
    print(Sensor)
    #gets the genome, insert location and the tn7 tranposes with the insert
    if len(input_data)> genome_map:
        #condition which permits when the insert location is inside the input_data
        final =input_data[:genome_map]+ Sensor +input_data[genome_map:]


        print(final)
        print("The Length of the genome carrying the desired gene is :")
        print(len(final))
    else:
        #If the location is input is wrong throws an error
        print("Enter correct gene location")

    return final

#function which inserts tn5 transposes in random sequence
def tn5(final, tn5_insert, Sensor):
    pu =[]
    #gets input from the user
    no_genome = int(input("How many variants of genome to be generated :"))
    print(no_genome)
    if no_genome >0:

        locations = [random.randrange(len(final)) for i in range(no_genome)]

        print(locations)

        for x in locations:
            # Here's where using a mutable list helps
            ak = str(final[:x]+ Sensor + final[x:])
            pu.append(ak)
            f= open("ak.txt", "w")
            f.write(ak)
            print(pu)
            print(len(ak))


    else:
        print("Enter the right number of variants")


Sensor, input_data = user_input()
tn7_insert = usage(Sensor)
tn5_insert = usage(Sensor)
genome_map = location_predictor()
final = tn7(genome_map,input_data, Sensor, tn7_insert)
tn5(final, tn5_insert, Sensor)
