/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package br.devlobo.projetoteste;

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
public class OlaTest {

    public OlaTest() {
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
    public void testDigaOla() {
        System.out.println(1);
        Ola instance = new Ola();

        String expResult = "hi";
        String result = instance.digaOla();
        assertEquals(expResult, result);
// TODO review the generated test code and remove the default call to fail.
//        fail("The test case is a prototype.");

    }

}
