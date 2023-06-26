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
### Alignment

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

### Description
 The top row represents your search sequence (Query). The bottom row represents a database sequence, called Subject (Sbjct). Lines connect the matching bases between Query and Subject. Missing lines indicate mismatches. Dashes (-) indicate gaps in the alignment. Gaps represent parts where Query or Subject have no counterpart. In the provided subject sequence, the "+" symbol represents a gap introduced to maximize the alignment with the query sequence. It indicates the presence of one or more residues in the subject sequence that are not present in the query sequence at that position. The gap helps to maintain the alignment and preserve the overall sequence similarity.
 
In the provided alignment, the numbers 601 and 600 refer to the positions or indices of the aligned residues in the query and subject sequences, respectively.


# outfmt_1

```

### Alignment

Query_1         1    MTMKYTLGANELSAKTHNLWKSILAEFIGIFILNFFSCAACTQAAFKTGIDTYTRITILA  60
XP_037300466.1  24         ..LD..AGGAAAIS.AL......NLL....G.GS.VNVGAAV.-----------  66
XP_037300468.1  8          ..LD..AGGAAAIS.AL......NLL....G.GS.VNVGAAV.-----------  50
XP_037300467.1  8          ..LD..AGGAAAIS.AL......NLL....G.GS.VNVGAAV.-----------  50
XP_016930642.1  5       E.S..L...KS.ELR..QALIG..L.NL.....A.G....I----------------  45
XP_016930412.1  18                 ENKKI.RML.G.LV.T.F.V.VGVGST.SGSV--------------  49
XP_036669236.1  15                 ENKKI.RML.G.LV.T.F.V.VGVGST.SGSV--------------  46
XP_037300778.1  20              ..EV.D.I.RQLI..LA.T.L.TSIGV.S.--------------...AE  56

```

### Description


In the format shown above, the identical residues are represented by a dot (.) and insertions and deletions are represented in the subject sequences, but not the query.

# outfmt_2

### Alignment 

### Description

This format is the same as Option 1 (Figure A-2), but all residues are shown with identities and positives in uppercase and mismatches in lowercase. As with Option 1, insertions and deletions are represented in the subject sequences, but not the query.

# outfmt_3

### Alignment 

### Description

Same as Option 1, but insertions or deletions in Figure A-4 are padded in the query, rather than shown in the subjects. This is a more compact format than the nonflat one, which has residues dangling down to represent insertions within the subject sequences.

# outfmt_4

### Alignment 

### Description

This format is the same as Option 2, but insertions or deletions in Figure A-5 are padded in the query, rather than shown in the subjects. Thus, the entire multiple sequence alignment is flat, without subject insertions dangling down.


REFERENCE :
https://etutorials.org/Misc/blast/Part+VI+Appendixes/Appendix+A.+NCBI+Display+Formats/A.2+Detailed+Descriptions+and+Examples/