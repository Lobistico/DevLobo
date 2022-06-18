/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/UnitTests/JUnit5TestClass.java to edit this template
 */
package com.mycompany.testeJUnit;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Aluno
 */
public class ResolucaoTRTest {

    public ResolucaoTRTest() {
    }

    @org.junit.jupiter.api.BeforeAll
    public static void setUpClass() throws Exception {
    }

    @org.junit.jupiter.api.AfterAll
    public static void tearDownClass() throws Exception {
    }

    @org.junit.jupiter.api.BeforeEach
    public void setUp() throws Exception {
    }

    @org.junit.jupiter.api.AfterEach
    public void tearDown() throws Exception {
    }

    /**
     * Test of metodo01 method, of class ResolucaoTR.
     */
    @org.junit.jupiter.api.Test
    public void testMetodo01() {
        System.out.println("metodo01");
        double base = 4.0;
        double altura = 2.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 4.0;
        double result = instance.metodo01(base, altura);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        // fail("The test case is a prototype.");
    }
    
    /**
     * Test of metodo02 method, of class ResolucaoTR.
     */
    @Test
    public void testMetodo02() {
        System.out.println("metodo02");
        double tempC = 5.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 41.0;
        double result = instance.metodo02(tempC);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        // fail("The test case is a prototype.");
    }

    /**
     * Test of metodo03 method, of class ResolucaoTR.
     */
    @org.junit.jupiter.api.Test
    public void test01Metodo03() {
        System.out.println("metodo03");
        ResolucaoTR instance = new ResolucaoTR();
        int expResult = 3;
        double valor = 14;
        int result = instance.metodo03(valor);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        // fail("The test case is a prototype.");
    }
    @org.junit.jupiter.api.Test
    public void test02Metodo03() {
        System.out.println("metodo03");
        ResolucaoTR instance = new ResolucaoTR();
        int expResult = 6;
        double valor = 327;
        int result = instance.metodo03(valor);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        // fail("The test case is a prototype.");
    }

    /**
     * Test of metodo04 method, of class ResolucaoTR.
     */
    @org.junit.jupiter.api.Test
    public void test01Metodo04() {
        System.out.println("metodo04");
        String msg = "5";
        ResolucaoTR instance = new ResolucaoTR();
        String expResult = "É Ímpar";
        String result = instance.metodo04(msg);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
    @org.junit.jupiter.api.Test
    public void test02Metodo04() {
        System.out.println("metodo04");
        String msg = "6";
        ResolucaoTR instance = new ResolucaoTR();
        String expResult = "É Par";
        String result = instance.metodo04(msg);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
    @org.junit.jupiter.api.Test
    public void test03Metodo04() {
        System.out.println("metodo04");
        String msg = "0";
        ResolucaoTR instance = new ResolucaoTR();
        String expResult = "É Par";
        String result = instance.metodo04(msg);
        assertEquals(expResult, result);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    //    FIM DO TESTE METODO 04


    /**
     * Test of Metodo05 method, of class ResolucaoTR.
     */
    @Test
    public void test01Metodo05() {
        System.out.println("Metodo05");
        double vel_via = 50.0;
        double vel_condutor = 60.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 50.00;
        double result = instance.Metodo05(vel_via, vel_condutor);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
     @Test
    public void test02Metodo05() {
        System.out.println("Metodo05");
        double vel_via = 50.0;
        double vel_condutor = 120.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 200.00;
        double result = instance.Metodo05(vel_via, vel_condutor);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
      @Test
    public void test03Metodo05() {
        System.out.println("Metodo05");
        double vel_via = 50.0;
        double vel_condutor = 70.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 100.00;
        double result = instance.Metodo05(vel_via, vel_condutor);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    @Test
    public void test04Metodo05() {
        System.out.println("Metodo05");
        double vel_via = 50.0;
        double vel_condutor = 49.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 0.00;
        double result = instance.Metodo05(vel_via, vel_condutor);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

    /**
     * Test of metodo06 method, of class ResolucaoTR.
     */
    @Test
    public void test01Metodo06() {
        System.out.println("metodo06");
        double primeironumero = 2.0;
        double segundonumero = 2.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 4.0;
        double result = instance.metodo06(primeironumero, segundonumero);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    @Test
    public void test02Metodo06() {
        System.out.println("metodo06");
        double primeironumero = 3.0;
        double segundonumero = 8.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 24.0;
        double result = instance.metodo06(primeironumero, segundonumero);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }

}
