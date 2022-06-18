package com.mycompany.testeJUnit;

import javax.swing.JOptionPane;

public class ResolucaoTR {

//    public static double numeros(String numero) {
//        String n = JOptionPane.showInputDialog(numero);
//        return Double.parseDouble(n);
//    }
//    
//    public void metodoJOptinM(String msg) {
//        JOptionPane.showMessageDialog(null, msg);
//    }
// EXERCICIO 01
    public double metodo01(double base, double altura) {
        double resultadoArea = (base * altura) / 2;
        return resultadoArea;
    }
// EXERCICIO 02

    public double metodo02(double tempC) {
        double tempF = ((9 * tempC + 160) / 5);
        return tempF;

    }

// EXERCICIO 03 
    public int metodo03(double valor) {

//        double valor = numeros("Digite o valor que deseja: ");       
        int notas = 0;

        boolean controlador = true;
        while (controlador) {
            if (valor >= 100) {
                valor -= 100;
                notas += 1;
            } else if (valor < 100 && valor >= 50) {
                valor -= 50;
                notas += 1;
            } else if (valor < 50 && valor >= 20) {
                valor -= 20;
                notas += 1;
            } else if (valor < 20 && valor >= 10) {
                valor -= 10;
                notas += 1;
            } else if (valor < 100 && valor >= 5) {
                valor -= 5;
                notas += 1;
            } else if (valor < 5 && valor >= 2) {
                valor -= 2;
                notas += 1;
            } else if (valor < 2 && valor >= 1) {
                valor -= 1;
                notas += 1;
            } else {
                controlador = false;
            }
        }
        return notas;
    }

//EXERCICIO 04
    public String metodo04(String msg) {
//        int numParImpar = Integer.parseInt(JOptionPane.showInputDialog(msg));;
        int numParImpar = Integer.parseInt(msg);

        if (numParImpar % 2 == 0) {
            return "É Par";
        } else {
            return "É Ímpar";
        }

    }
    
    /*
3.5 EXERCÍCIO 05
Crie um método chamado metodo05 que receba como parâmetros a velocidade máxima 
permitida em uma avenida e a velocidade de um motorista, calcule e retorne
o valor da multa que esse motorista deve receber, sabendo que são pagos:
*/
   
    public double Metodo05(double vel_via, double vel_condutor) {

        if (((vel_condutor - vel_via) <= 10) && ((vel_condutor - vel_via) > 0)) {
            return 50.00;
        } else if (((vel_condutor - vel_via) > 10) && ((vel_condutor - vel_via) < 30)) {
            return 100.00;
        } else if ((vel_condutor - vel_via) > 30) {
            return 200;
        } else {
            return 0;
        }
    }
    
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




