# -*- coding: iso-8859-15 -*-

from h800.punchcard import PunchCard, Deck


def test_simple():
    # TODO: simple tester.
    line = " 0981   BACKUP     TS           S ZERO        COMMON        SET UP GPB     C    COMMUNICATION FLAG FOR END."
    c = PunchCard(line)
    assert c.line == line
    assert c.layout == [(1, 1), (2, 6), (8, 1), (9, 11), (20, 13), (33, 14),
                        (47, 14), (61, 15), (76, 5), (81, 40)]
    assert c.fields == [' ', '0981  ', ' ', 'BACKUP     ', 'TS           ',
                        'S ZERO        ', 'COMMON        ', 'SET UP GPB     ',
                        'C    ', 'COMMUNICATION FLAG FOR END.']
    assert c.strippedFields == [None, '0981', None, 'BACKUP', 'TS', 'S ZERO',
                                'COMMON', 'SET UP GPB', 'C',
                                'COMMUNICATION FLAG FOR END.']
    assert len(c.record) == 10
    assert c.record == {"column1": None, "lognum": '0981', "column8": None,
                        "label": 'BACKUP', "operation": 'TS',
                        "operand1": 'S ZERO', "operand2": 'COMMON',
                        "operand3": 'SET UP GPB', "misc": 'C',
                        "remarks": 'COMMUNICATION FLAG FOR END.'}
    print("PASS")

    lines = """
L      @XYZ TESTING 123

 0020   L BACKUP   SPEC                                       BACKUP
 0021   L PRINT PS SPEC                                       PRINT PS

 0030   A999999    ALF          09999990
 0031   ASTRISK    ALF          *
 0032   COMA 1962  ALF          , 1962
 0033   DASH 1T3   ALF          ---

 0035   PASSS RE   ALF          RE: ASSE
 0036   MANUS RE   ALF            RE: MA
 0038   PASS S EQU ALF            = ASSE
 0039   MANU S EQU ALF              = MA
 0046   Y COLYUM 1 ALF          Y      3
 0047   PMAX9 MSJ  ALF          PMAX = 9
 0048   S BLANKS   ALF

 0049   S BLOTS    ALF          ████████
 0050   S COLON C1 ALF          :
 00505  S SIGH     ALF          (SIGH)

 0055   W 254P     ALF          254+

# Page 110
L      @YUL SYSTEM PASS 0 SERVICE MODULE                                         USER'S OWN PAGE NO.   3        PAGE  70

P0068   ONE-WORD ALPHABETIC CONSTANTS CONCLUDED.

 0069   W NONE     ALF           (NONE)
 0070   W OBS      ALF            *OBS*
 0071   W OBSOLET  ALF          OBSOLETE
 0085   ZSUP ONE   ALF                 1


R0086   ALPHABETIC ARRAYS.

 0088   BKUP LINE  ALF,4         DIRECTORY LISTING OF YULPROGS #
 0089   BUREL MSG  ALF,2        BACKUP RELABELED
 0090   CHEDL MSG  ALF,3        CHECK DIRECTORY LISTING
 0091   COMPU MSG  ALF,2
 0092   COMUS MSG  ALF,3        COMPUTER IS STILL IN USE
 0093   CONCN MSG  ALF,5        CONFLICT WITH EXISTING COMPUTER NAME-
 0094   DCLAV MSG  ALF,3        DECLARED AVAILABLE
 0095   DCLOB MSG  ALF,3        DECLARED OBSOLETE
 0096   DCLOK MSG  ALF,3        DECLARED CHECKED OUT
 0097   MANUS MSG  ALF,2        NUFACTURING FOR

# Page 111
L      @YUL SYSTEM PASS 0 SERVICE MODULE                                         USER'S OWN PAGE NO.   4        PAGE  71

P0098   ALPHABETIC ARRAYS CONTINUED.

 0099   MNTN LINE  ALF,4        YUL SYSTEM MAINTENANCE FUNCTION:
 0100   NEWCO MSG  ALF,3          NEW COMPUTER:
 0101   NEW LINE   OCT          0
 0102              ALF,5
 0103              ALF,5
 0104              ALF,5
 0105   NOMAT MSG  ALF,4        NO MATCH FOUND FOR THIS CARD:
 0106   NOTAV MSG  ALF,2        NOT AVAILABLE
 0107   NOW OP MSG ALF,4         NOW OPERATING FROM NEW YULPROGS

 0108   OBUWK MSG  ALF,4        FORMER BACKUP WILL BE WORKER
 0109   OP SLP MSJ ALF,2        OPERATOR ASLEEP
 0110   PASSS MSG  ALF,2        MBLY PASS █ FOR
 0111   PCH CARD   OCT          0
 0112              ALF,5
 0113              ALF,5
 0932   RUNOUT PR  TS           S 4SPACE      N,X2,1        GET LOG NO     C
 0933              SWS, D8T12   S ZERO                      N,AU2
 0934              MT           S BLANKS      15            N,X2,1
 0935              WD           Z,X2          OCTAL 20      Z,X2
 0936              S, PHI PRINT 2,0
 0937              S, PHI PRINT 2,0
 0938              S, PHI PRINT 2,0                                             FORCE LAST LINES THROUGH BUFPRINT.
 0940              S, MON TYPER W LIST DUN    SPRAMR +16    -                   ANNOUNCE END OF LISTING.

R0979   TO EACH.  WHEN THE LISTING IS FINISHED, GROUP B HOISTS A FLAG AND EXPIRES.


 0981   BACKUP     TS           S ZERO        COMMON        SET UP GPB     C    COMMUNICATION FLAG FOR END.
 0983              TS           Z,SC,4        N,SH          MON WAKE       C

 0984   BK1 VIA X0 TX           L BANK 1      -             Z,X0
 0985              TX           L DIRECTY     -             Z,X1
 0986              TX           PHI WAA       -             Z,X6
 0987              TS           YUL MASKS     Z,MXR         LIST LABL           START GROUP B GOING ON LISTING.

 0989              TX           1,1           -             YUL BU MSG +1
 0991              NA, CHAR8    1,0           S ONE         AMEND BUL           BRANCH IF ONLY MUST AMEND BACKUP LABEL.
""".splitlines()

    d = Deck(lines)

    import pprint
    pprint.pprint(d.records)
