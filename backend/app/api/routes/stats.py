
from fastapi import APIRouter, HTTPException, status, Depends, Request


router = APIRouter(prefix="/stats")

@router.get("/sharpee_ratio/", tags=["stats"])
def get_sharpee_ratio():
    pass

@router.get("/sortino_ratio/", tags=["stats"])
def get_sortino_ratio():
    pass

@router.get("/maximum_drawdown/", tags=["stats"])
def get_maximum_drawdown():
    pass

@router.get("/calmar_ratio/", tags=["stats"])
def get_calmar_ratio():
    pass

@router.get("/treynor_ratio/", tags=["stats"])
def get_treynor_ratio():
    pass

@router.get("/beta/", tags=["stats"])
def get_beta():
    pass

@router.get("/alpha/", tags=["stats"])
def get_alpha():
    pass

@router.get("/information_ratio/", tags=["stats"])
def get_information_ratio():
    pass

@router.get("/omega_ratio/", tags=["stats"])
def get_omega_ratio():
    pass

@router.get("/value_at_risk/", tags=["stats"])
def get_value_at_risk():
    pass

