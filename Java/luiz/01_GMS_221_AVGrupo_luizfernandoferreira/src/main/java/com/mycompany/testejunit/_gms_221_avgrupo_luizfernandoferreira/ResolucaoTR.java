package com.mycompany.testejunit._gms_221_avgrupo_luizfernandoferreira;

public class ResolucaoTR 
{
    //EXERCICIO 06
    //Retorna o produto entre dois números
    public double metodo06(double primeironumero, double segundonumero)
    {
        double resultado = 0;
        for(int i = 0; i < primeironumero; i++)
        {
            resultado = resultado + segundonumero;
        }        
        return resultado;
    }
}
