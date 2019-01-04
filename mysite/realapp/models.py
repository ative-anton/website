import datetime

from django.db import models
from django.utils import timezone


class QuestionReal(models.Model):
    # Program Page
    # investor
    investor_text = models.CharField(max_length=200)
    # program
    program_text = models.CharField(max_length=200)

    # Matrix Page
    # loan amount
    loan_amt_text = models.CharField(max_length=200)
    # reserve
    reserve_text = models.CharField(max_length=200)
    # FICO
    fico_text = models.CharField(max_length=200)
    # Full Doc or Alternative Doc
    doc_text = models.CharField(max_length=200)
    # Purchase & R/T
    purch_rt_text = models.CharField(max_length=200)
    # Cash Out
    cash_out_text = models.CharField(max_length=200)
    # DTI
    dti_text = models.CharField(max_length=200)
    # LTV
    ltv_text = models.CharField(max_length=200)
    # Second Home
    second_home_text = models.CharField(max_length=200)
    # Property Type
    prop_type_text = models.CharField(max_length=200)
    # IO Period
    io_text = models.CharField(max_length=200)
    # Amort Term
    amort_text = models.CharField(max_length=200)
    # Final Maturity
    final_matur_text = models.CharField(max_length=200)


class Answer(models.Model):
    question = models.ForeignKey(QuestionReal, on_delete=models.CASCADE)
    # Program Page
    # investor
    investor_aws = models.CharField(max_length=200)
    # program
    program_aws = models.CharField(max_length=200)

    # Matrix Page
    # loan amount
    loan_amt_aws = models.CharField(max_length=200)
    # reserve
    reserve_aws = models.CharField(max_length=200)
    # FICO
    fico_aws = models.CharField(max_length=200)
    # Full Doc or Alternative Doc
    doc_aws = models.CharField(max_length=200)
    # Purchase & R/T
    purch_rt_aws = models.CharField(max_length=200)
    # Cash Out
    cash_out_aws = models.CharField(max_length=200)
    # DTI
    dti_aws = models.CharField(max_length=200)
    # LTV
    ltv_aws = models.CharField(max_length=200)
    # Second Home
    second_home_aws = models.CharField(max_length=200)
    # Property Type
    prop_type_aws = models.CharField(max_length=200)
    # IO Period
    io_aws = models.CharField(max_length=200)
    # Amort Term
    amort_aws = models.CharField(max_length=200)
    # Final Maturity
    final_matur_aws = models.CharField(max_length=200)

