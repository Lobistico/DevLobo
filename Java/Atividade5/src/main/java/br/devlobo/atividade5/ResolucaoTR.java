/*
3.5 EXERCÍCIO 05
Crie um método chamado metodo05 que receba como parâmetros a velocidade máxima 
permitida em uma avenida e a velocidade de um motorista, calcule e retorne
o valor da multa que esse motorista deve receber, sabendo que são pagos:

I. 0 (zero) reais se não houver multa;

II. 50 reais se o motorista tiver ultrapassado em até 10km/h a velocidade
permitida (ex.: velocidade máxima: 50km/h; motorista a 60km/h ou a 56km/h);

III. 100 reais, se o motorista ultrapassar acima de 10 até 30 km/h a velocidade
permitida.

IV. 200 reais, se estiver acima de 30km/h da velocidade permitida
 */
package br.devlobo.atividade5;

/**
 *
 * @author lobo
 */
public class ResolucaoTR {

    public double Metodo1(double vel_via, double vel_condutor) {

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
}
