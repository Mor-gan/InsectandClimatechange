# InsectandClimatechange

## blastp options and possible output
```
 *** Formatting options
 -outfmt <String>
alignment view options:
```
   **0 = Pairwise** 
   
   - Standard BLAST alignment in pairs of query sequence and database match.  


  **1 = Query-anchored showing identities,**

  - The databases alignments are anchored (shown in relation to) to the query sequence. Identities are displayed as dashes, with mismatches displayed as single letter nucleotide abbreviations.
  
  **2 = Query-anchored no identities,**
- The 'flat' display shows inserts as deletions on the query. 

**3 = Flat query-anchored showing identities,**
- The 'flat' display shows inserts as deletions on the query. Identities are displayed as dashes, with mismatches displayed as single letter nucleotide abbreviations.


**4 = Flat query-anchored no identities,**
- The 'flat' display shows inserts as deletions on the query. Identities are shown as single letter nucleotide abbreviations.

**5 = BLAST XML,**

**6 = Tabular,**

**7 = Tabular with comment lines,**

**8 = Seqalign (Text ASN.1),**

**9 = Seqalign (Binary ASN.1),**

**10 = Comma-separated values,**


11 = BLAST archive (ASN.1),

12 = Seqalign (JSON),

13 = Multiple-file BLAST JSON,

14 = Multiple-file BLAST XML2,

15 = Single-file BLAST JSON,

16 = Single-file BLAST XML2,

18 = Organism Report

#  outfmt-0 : 

```
## Alignment

Query  1    MPAIGIDLGTTYSCVGVYQHGKVEIIANDQGNRTTPSYVAFTDSERLIGDPAKNQVAMNP  60
            MPAIGIDLGTTYSCVGVYQHGKVEIIANDQGNRTTPSYVAFTDSERLIGD AKNQVAMNP
Sbjct  1    MPAIGIDLGTTYSCVGVYQHGKVEIIANDQGNRTTPSYVAFTDSERLIGDAAKNQVAMNP  60


Query  541  ESYVFNVKQAVEQAPAGKLDEADKNSVLDKCNDTIRWLDSNTTAEKEEFDHKLEELTRHC  600
            E+YVF+VKQA++ A   KL E+DK++    C++ +RWLD+NT AE+EE++HKL++L R C
Sbjct  541  EAYVFSVKQALDDA-GDKLSESDKSTARSACDEALRWLDNNTLAEQEEYEHKLKDLQRVC  599


Query  601  SPIMTKMHQQGAGAGAGGPGANCGQQAGGFGGYSGPTVEEVD  642
            SP+MTKMH            A  GQQ    G   GPTVEEVD
Sbjct  600  SPVMTKMHGGAGAG-----AAPGGQQ---HGRADGPTVEEVD  633
```

## Description
 The top row represents your search sequence (Query). The bottom row represents a database sequence, called Subject (Sbjct). Lines connect the matching bases between Query and Subject. Missing lines indicate mismatches. Dashes (-) indicate gaps in the alignment. Gaps represent parts where Query or Subject have no counterpart. In the provided subject sequence, the "+" symbol represents a gap introduced to maximize the alignment with the query sequence. It indicates the presence of one or more residues in the subject sequence that are not present in the query sequence at that position. The gap helps to maintain the alignment and preserve the overall sequence similarity.
 
In the provided alignment, the numbers 601 and 600 refer to the positions or indices of the aligned residues in the query and subject sequences, respectively.