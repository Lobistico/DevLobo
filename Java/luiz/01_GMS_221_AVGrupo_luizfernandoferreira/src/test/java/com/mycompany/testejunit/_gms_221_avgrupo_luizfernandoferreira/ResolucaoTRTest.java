/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package com.mycompany.testejunit._gms_221_avgrupo_luizfernandoferreira;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author Fernando
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
    
    /**@BeforeAll
    public static void setUpClass() {
    }
    
    @AfterAll
    public static void tearDownClass() {
    }
    
    @BeforeEach
    public void setUp() {
    }
    
    @AfterEach
    public void tearDown() {
    }*/

    /**
     * Test of metodo06 method, of class ResolucaoTR.
     */
    @org.junit.jupiter.api.Test
    public void testMetodo06() 
    {
        System.out.println("metodo06");
        double primeironumero = 1.0;
        double segundonumero = 2.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 2.0;
        double result = instance.metodo06(primeironumero, segundonumero);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype. FALHA");
    }
   
}
