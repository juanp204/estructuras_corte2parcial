using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrafoNoDirigido
{
    internal class Arista
    {
        /* 
         Esta es la clase arista, guarda la información del peso y los vértices que conecta!
         */

        //Propiedades
        private int weight;
        private Vertice v1, v2;

        //Get y Sets
        public int Weight { get { return weight; } set { weight = value; } }
        public Vertice V1 { get { return v1; } set { v1 = value; } }
        public Vertice V2 { get { return v2; } set { v2 = value; } }

        //Constructor
        public Arista(int weight, Vertice v1, Vertice v2)
        {
            this.weight = weight;
            this.v1 = v1;
            this.v2 = v2;
        }

        public override string ToString()
        {
            return v1.ID + " " + v2.ID;
        }
    }
}
