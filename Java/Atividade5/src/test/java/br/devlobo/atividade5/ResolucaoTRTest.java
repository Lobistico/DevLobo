/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.devlobo.atividade5;

import org.junit.jupiter.api.AfterEach;
import org.junit.jupiter.api.AfterAll;
import org.junit.jupiter.api.BeforeEach;
import org.junit.jupiter.api.BeforeAll;
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

/**
 *
 * @author lobo
 */
public class ResolucaoTRTest {
    
    public ResolucaoTRTest() {
    }
    
    @BeforeAll
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
    }

   
    @Test
    public void testMetodo1() {
        System.out.println("Metodo1");
        double vel_via = 50.0;
        double vel_condutor = 60.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 50.00;
        double result = instance.Metodo1(vel_via, vel_condutor);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
     @Test
    public void testMetodo2() {
        System.out.println("Metodo1");
        double vel_via = 50.0;
        double vel_condutor = 120.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 200.00;
        double result = instance.Metodo1(vel_via, vel_condutor);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
      @Test
    public void testMetodo3() {
        System.out.println("Metodo1");
        double vel_via = 50.0;
        double vel_condutor = 70.0;
        ResolucaoTR instance = new ResolucaoTR();
        double expResult = 20.00;
        double result = instance.Metodo1(vel_via, vel_condutor);
        assertEquals(expResult, result, 0.0);
        // TODO review the generated test code and remove the default call to fail.
        //fail("The test case is a prototype.");
    }
    
}
