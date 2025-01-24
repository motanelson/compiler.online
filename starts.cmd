@echo off
@IF NOT EXIST .\uploads\%1 mkdir .\uploads\%1 
@copy .\uploads\%1.bas .\uploads\%1\%1.bas