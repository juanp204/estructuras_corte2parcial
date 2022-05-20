using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrafoNoDirigido
{
    internal class Program
    {
        static void Main(string[] args)
        {
            /*El enunciado de la situación problema se encuentra en la clase de grafo no dirigido, utilice este
            * espacio para realizar las pruebas que considere necesarias para asegurar el funcionamiento de su clase. 
            * (y de la lista de amigos de Jonny). */

            //Prueba de la clase grafo:
            //Creamos el grafo: (Es importante el new, si no se crearía una variable vacía!)
            GrafoNoDirigido grafoTest = new GrafoNoDirigido();

            Console.WriteLine("Prueba del método para añadir vértices: ");

            grafoTest.addVertice("A"); //El primer vértice no tiene adyacencia!
            grafoTest.addVertice("B", 4, new object[1] { grafoTest.searchVerticeID("A") }); //El segundo tiene una arista con el primero!
            grafoTest.addVertice("C", 5, new object[2] { grafoTest.searchVerticeID("A"), grafoTest.searchVerticeID("B") }); //Observe que C tiene aristas con A y B!
            grafoTest.addVertice("D", 7, new object[1] { grafoTest.searchVerticeID("C") }); //Por su parte D solo tiene una arista con C.

            //Recomendación: Realice un dibujo del grafo! Esto le ayuda a comprender la estructura que tiene y lo que está escrito arriba.

            /*¡Probemos imprimiendo el grafo por consola!
             * Recuerde que en la clase grafo se hizo un override al método ToString. En C# esto altera el comportamiento del objeto cuando se pone dentro de un WriteLine,
             * pues internamente el método convierte en string todo lo que se encuentre dentro de los paréntesis (!), por este motivo solo es necesario poner el objeto dentro
             * del WriteLine y voilà! El método reescrito ToString funcionará automáticamente. RECUERDE QUE ESTO NO SE CUMPLE PARA TODOS LOS LENGUAJES DE PROGRAMACIÓN !!!!!
             * Si se encuentra con un error consulte como funciona el método para imprimir que esté utilizando. */
            Console.WriteLine(grafoTest);

            /*Observe que el resultado en consola muestra la información del grafo. ¡Genial! Tenemos un grafo no dirigido en nuestras manos .... ¿y ahora?
            Probemos algunos otros métodos que exploran algunas propiedades de la estructura de datos:
            */

            Console.WriteLine("\nPrueba del método getByIDVertice: ");

            //El mismo comportamiento se aplica para este WriteLine, getByIDVertice permite consultar la información de un vértice. Como tiene un ToString reescrito, solo basta con ponerlo.
            Console.WriteLine(grafoTest.getByIDVertice(0));

            Console.WriteLine("\nPrueba del método getAdjacentVertices: ");
            Console.WriteLine(String.Join(", ", grafoTest.getAdjacentVertices(2)));
            //Observe que este WriteLine necesita un método extra para mostrar correctamente la información por consola. Esto se debe a que el método getAdjacentVertices
            //devuelve un Array, que no tiene nuestro override!

            Console.WriteLine("\nPrueba del método getEdgeGrado: ");
            Console.WriteLine(grafoTest.getEdgeGrado(0)); //Primer vértice
            Console.WriteLine(grafoTest.getEdgeGrado(1)); //Segundo vértice
            Console.WriteLine(grafoTest.getEdgeGrado(2)); // .....
            Console.WriteLine(grafoTest.getEdgeGrado(3));

            Console.WriteLine("\nPrueba del método NumberVertices: ");
            Console.WriteLine(grafoTest.NumberVertices());

            //Felicitaciones! Si ha llegado a este punto y todo funciona correctamente ya tiene un grafo no dirigido funcional en su disco duro.
            Console.ReadLine();
        }
    }
}
