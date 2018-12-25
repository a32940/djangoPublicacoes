from django.db import models

class publicacoes(models.Model):
    PT= models.CharField(max_length=200000,null=True, blank=True)
    AU= models.CharField(max_length=200000,null=True, blank=True)	
    BA= models.CharField(max_length=200000,null=True, blank=True)
    BE= models.CharField(max_length=200000,null=True, blank=True)
    GP= models.CharField(max_length=200000,null=True, blank=True)
    AF= models.CharField(max_length=200000,null=True, blank=True)
    BF= models.CharField(max_length=200000,null=True, blank=True)
    CA= models.CharField(max_length=200000,null=True, blank=True)
    TI= models.CharField(max_length=200000,null=True, blank=True)
    SO= models.CharField(max_length=200000,null=True, blank=True)
    SE= models.CharField(max_length=200000,null=True, blank=True)
    BS= models.CharField(max_length=200000,null=True, blank=True)
    LA= models.CharField(max_length=200000,null=True, blank=True)
    DT= models.CharField(max_length=200000,null=True, blank=True)
    CT= models.CharField(max_length=200000,null=True, blank=True)
    CY= models.CharField(max_length=200000,null=True, blank=True)
    CL= models.CharField(max_length=200000,null=True, blank=True)
    SP= models.CharField(max_length=200000,null=True, blank=True)
    HO= models.CharField(max_length=200000,null=True, blank=True)
    DE= models.CharField(max_length=200000,null=True, blank=True)
    ID_f= models.CharField(max_length=200000,null=True, blank=True)
    AB= models.CharField(max_length=200000,null=True, blank=True)
    C1= models.CharField(max_length=200000,null=True, blank=True)
    RP= models.CharField(max_length=200000,null=True, blank=True)
    EM= models.CharField(max_length=200000,null=True, blank=True)
    RI= models.CharField(max_length=200000,null=True, blank=True)
    OI= models.CharField(max_length=200000,null=True, blank=True)
    FU= models.CharField(max_length=200000,null=True, blank=True)
    FX= models.CharField(max_length=200000,null=True, blank=True)
    CR= models.CharField(max_length=200000,null=True, blank=True)
    NR= models.CharField(max_length=200000,null=True, blank=True)
    TC= models.CharField(max_length=200000,null=True, blank=True)
    Z9= models.CharField(max_length=200000,null=True, blank=True)
    U1= models.CharField(max_length=200000,null=True, blank=True)
    U2= models.CharField(max_length=200000,null=True, blank=True)
    PU= models.CharField(max_length=200000,null=True, blank=True)
    PI= models.CharField(max_length=200000,null=True, blank=True)
    PA= models.CharField(max_length=200000,null=True, blank=True)
    SN= models.CharField(max_length=200000,null=True, blank=True)
    EI= models.CharField(max_length=200000,null=True, blank=True)
    BN= models.CharField(max_length=200000,null=True, blank=True)
    J9= models.CharField(max_length=200000,null=True, blank=True)
    JI= models.CharField(max_length=200000,null=True, blank=True)
    PD= models.CharField(max_length=200000,null=True, blank=True)
    PY= models.CharField(max_length=200000,null=True, blank=True)
    VL= models.CharField(max_length=200000,null=True, blank=True)
    IS= models.CharField(max_length=200000,null=True, blank=True)
    PN= models.CharField(max_length=200000,null=True, blank=True)
    SU= models.CharField(max_length=200000,null=True, blank=True)
    SI= models.CharField(max_length=200000,null=True, blank=True)
    MA= models.CharField(max_length=200000,null=True, blank=True)
    BP= models.CharField(max_length=200000,null=True, blank=True)
    EP= models.CharField(max_length=200000,null=True, blank=True)
    AR= models.CharField(max_length=200000,null=True, blank=True)
    DI= models.CharField(max_length=200000,null=True, blank=True)
    D2= models.CharField(max_length=200000,null=True, blank=True)
    EA= models.CharField(max_length=200000,null=True, blank=True)
    EY= models.CharField(max_length=200000,null=True, blank=True)
    PG= models.CharField(max_length=200000,null=True, blank=True)
    WC= models.CharField(max_length=200000,null=True, blank=True)
    SC= models.CharField(max_length=200000,null=True, blank=True)
    GA= models.CharField(max_length=200000,null=True, blank=True)
    UT= models.CharField(max_length=200000,null=True, blank=True)
    PM= models.CharField(max_length=200000,null=True, blank=True)
    OA= models.CharField(max_length=200000,null=True, blank=True)
    HC= models.CharField(max_length=200000,null=True, blank=True)
    HP= models.CharField(max_length=200000,null=True, blank=True)
    DA= models.CharField(max_length=200000,null=True, blank=True)
    Hospital = models.CharField(max_length=50,null=True, blank=True)
    UalgAfiliacao =  models.CharField(max_length=50,null=True, blank=True)
    unidadeOriganica = models.CharField(max_length=1000,null=True, blank=True)
    centroInvestigacao = models.CharField(max_length=1000,null=True, blank=True)
    pais= models.CharField(max_length=1000,null=True, blank=True)
    class Meta:
        verbose_name = 'Publicação'
        verbose_name_plural = 'Publicações'

class termosUalg(models.Model):
    termo = models.CharField(max_length=1000,null=True, blank=True)
    def __str__(self):
    	return (self.termo)
    class Meta:
        verbose_name = 'Termo de procura ualg'
        verbose_name_plural = 'Termos de procura ualg'

class termosHospital(models.Model):
    termo = models.CharField(max_length=1000,null=True, blank=True)
    def __str__(self):
    	return (self.termo)
    class Meta:
        verbose_name = 'Termo de procura hospital'
        verbose_name_plural = 'Termos de procura hospital'

class termosUnidadeOrganica(models.Model):
    termo = models.CharField(max_length=1000,null=True, blank=True)
    def __str__(self):
    	return (self.termo)
    class Meta:
        verbose_name = 'Termo de procura UO'
        verbose_name_plural = 'Termos de procura UO'

class centroInvestigacao(models.Model):
    termo = models.CharField(max_length=1000,null=True, blank=True)
    def __str__(self):
    	return (self.termo)
    class Meta:
        verbose_name = 'Termo de procura centro de investigacao'
        verbose_name_plural = 'Termos de procura centro de investigacao'

class paises(models.Model):
    termo = models.CharField(max_length=1000,null=True, blank=True)
    def __str__(self):
    	return (self.termo)
    class Meta:
        verbose_name = 'Termo de procura paises'
        verbose_name_plural = 'Termos de procura paises'