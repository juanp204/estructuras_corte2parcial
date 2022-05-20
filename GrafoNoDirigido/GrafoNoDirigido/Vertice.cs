using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrafoNoDirigido
{
    internal class Vertice
    {
        public int ID;
        private object dato;        
        private Lista adyacentes = new Lista();
        public object Dato
        {
            get { return dato; }
        }

        public Vertice(int ID, object Dato)
        {
            this.ID = ID;
            dato = Dato;
        }

        public bool addEdge(int ID)
        {
            bool checker = false;

            if (this.ID != ID)
            {               
                if(adyacentes.add(ID)) checker = true;
            }

            return checker;
        }

        public Lista getAdjacentVertices()
        {
            return adyacentes;
        }

        public override string ToString()
        {
            return "ID: " + ID + " Dato: " + Dato + " Adj: " + String.Join(", ", getAdjacentVertices()) + "\n";
        }
    }
}
