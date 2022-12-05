'''This is a study to assess the execution quality of FINRA 
reported trades vs lit-market trades by assessing how far off the NBBO each trade was. 

The study uses 1000 trades each from 33 low volume issues screened on 11/19/22 with prices between $10 
and $50 and daily volume between 5000 and 25000 shares done on market screener

Get the trades, NBBO bid ask, and the executing exchange and see how close the 
FINRA (PFOF, Internalized, Dark Pool reported trades) are to the NBBO vs all the
 other trades (lit). My hypothese is that FINRA will offer the worst fills.

SYMBOL,COMPANY NAME,PRICE,CHG,CHG %,VOL

DLHC,DLH Holdings Corp.,$13.30 ,-0.1,-0.75%,6.36K
DSGR,Distribution Solutions Group Inc.,$37.56 ,-0.36,-0.95%,19.22K
EBTC,Enterprise Bancorp Inc.,$34.29 ,0.63,1.87%,13.04K
ECBK,ECB Bancorp Inc.,$16.75 ,0.05,0.30%,14.66K
EDRY,EuroDry Ltd.,$16.19 ,0.19,1.19%,18.41K
EMCF,Emclaire Financial Corp.,$32.65 ,-1.22,-3.60%,5.51K
ENCP,Energem Corp. Cl A,$10.36 ,0.06,0.57%,11.68K
ESSA,ESSA Bancorp Inc.,$21.42 ,0.24,1.13%,13.27K
EVI,EVI Industries Inc.,$18.65 ,-0.14,-0.75%,7.85K
FBIZ,First Business Financial Services Inc.,$39.39 ,0.14,0.36%,16.23K
FET,Forum Energy Technologies Inc.,$28.71 ,-0.06,-0.21%,18.31K
FFBW,FFBW Inc.,$11.75 ,-0.13,-1.07%,5.95K
FGBI,First Guaranty Bancshares Inc.,$23.91 ,-0.19,-0.79%,7.25K
FLXS,Flexsteel Industries Inc.,$15.44 ,0.79,5.39%,14.43K
FMAO,Farmers & Merchants Bancorp Inc.,$28.58 ,0.06,0.21%,18.03K
FNLC,First Bancorp Inc.,$31.20 ,0.3,0.97%,15.77K
FRBA,First Bank (NJ),$15.25 ,0.15,0.99%,17.91K
FRBN,Forbion European Acquisition Corp. Cl A,$10.21 ,-0.01,-0.05%,5.7K
FRST,Primis Financial Corp.,$12.48 ,0.09,0.73%,24.7K
FRW,PWP Forward Acquisition Corp. I Cl A,$10.04 ,0.01,0.05%,24.64K
FSBC,Five Star Bancorp,$28.33 ,0.08,0.28%,19.22K
FSBW,FS Bancorp Inc.,$33.10 ,0.11,0.33%,5.73K
FSFG,First Savings Financial Group Inc.,$23.03 ,0.24,1.05%,8.37K
FSTR,L.B. Foster Co.,$11.00 ,0.07,0.64%,16.71K
FVCB,FVCBankcorp Inc.,$19.87 ,-0.1,-0.50%,18.82K
GECC,Great Elm Capital Corp.,$10.23 ,0.03,0.31%,8.23K
GHM,Graham Corp.,$10.15 ,0.15,1.50%,7.79K
GNTY,Guaranty Bancshares Inc.,$35.80 ,0.4,1.13%,6.84K
GRRR,Gorilla Technology Group Inc.,$10.80 ,-0.63,-5.53%,5.28K
GRVY,GRAVITY Co. Ltd. ADR,$45.27 ,0.36,0.80%,5.11K
HBB,Hamilton Beach Brands Holding Co. Cl A,$13.22 ,-0.52,-3.78%,15.76K
HBCP,Home Bancorp Inc.,$42.63 ,0.35,0.83%,11.49K
HQI,HireQuest Inc.,$16.60 ,1.7,11.41%,19.53K
HSON,Hudson Global Inc.,$22.38 ,-0.06,-0.25%,13.18K
HURC,Hurco Cos.,$25.65 ,0.42,1.66%,6.49K
IESC,IES Holdings Inc.,$33.17 ,0.05,0.15%,9.88K
'''