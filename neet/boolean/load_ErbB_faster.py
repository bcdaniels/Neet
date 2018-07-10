# test_load_ErbB_faster.py
#
# Bryan Daniels
# 7.5.2018
#
# if we predefine functions, is it faster to load into Neet?
#

def ShcFunc(binaryVec):
    EGFR_Y992,ErbB2_ErbB4,EGFR_EGFR_TGFa_PM,EGFR_EGFR_TGFa_End,EGFR_ErbB4,ErbB3_ErbB4,EGFR_EGFR_EGF_End,EGFR_EGFR_TGFa_CCV,EGFR_ErbB2,EGFR_EGFR_TGFa_CCP,EGFR_EGFR,EGFR_EGFR_EGF_CCV,EGFR_EGFR_EGF_PM,EGFR_EGFR_EGF_MVB,EGFR_EGFR_EGF_CCP,EGFR_ErbB3,PTEN,Fak,EGFR_Y1173,ErbB2_Y1196,Src,ErbB4_Y1242,ErbB4_Y1188,ErbB2_Y1221_22,ErbB3_Y1309,ErbB2_Y1248,EGFR_Y1148 = binaryVec
    
    ANY_EGFR = ErbB2_ErbB4  or EGFR_EGFR_TGFa_PM  or EGFR_EGFR_TGFa_End  or EGFR_ErbB4  or ErbB3_ErbB4  or EGFR_EGFR_EGF_End  or EGFR_EGFR_TGFa_CCV  or EGFR_ErbB2  or EGFR_EGFR_TGFa_CCP  or EGFR_EGFR  or EGFR_EGFR_EGF_CCV  or EGFR_EGFR_EGF_PM  or EGFR_EGFR_EGF_MVB  or EGFR_EGFR_EGF_CCP  or EGFR_ErbB3
    
    Shc = ( ( EGFR_Y992 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( Fak  ) and not ( PTEN  ) )  or ( ( EGFR_Y1173 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( ErbB2_Y1196 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( Src  ) and not ( PTEN  ) )  or ( ( ErbB4_Y1242 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( ErbB4_Y1188 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( ErbB2_Y1221_22 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( ErbB3_Y1309 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( ErbB2_Y1248 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )  or ( ( EGFR_Y1148 and ( ( ( ANY_EGFR ) ) )     ) and not ( PTEN  ) )

    return Shc
