using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace GrafoNoDirigido
{
    internal class GrafoNoDirigido
    {
        int idAssigner = 0;
        Lista listaVertices = new Lista(), listaArista = new Lista();

        public bool addVertice(object objeto, int peso = 0, object[] adyacencia = null)
        {
            bool checker = false;
            var vertexCurrent = new Vertice(idAssigner, objeto);

            listaVertices.add(vertexCurrent);

            if (adyacencia != null)
            {
                for (int e = 0; e < adyacencia.Length; e++)
                {
                    var vertex = getByIDVertice(int.Parse(adyacencia[e].ToString()));
                    vertex.addEdge(idAssigner);
                    vertexCurrent.addEdge(vertex.ID);
                    var aristaTemp = new Arista(peso, vertexCurrent, vertex);
                    if (!listaArista.contains(aristaTemp)) { listaArista.add(aristaTemp); }
                }
            }

            idAssigner++;
            checker = true;

            return checker;
        }

        public int searchVerticeID(object objeto)
        {
            var tempArraySearch = listaVertices.toArray();
            int id = -1;

            for (int i = 0; i < tempArraySearch.Length; i++)
            {
                if (((Vertice)tempArraySearch[i]).Dato.ToString() == objeto.ToString())
                {
                    id = ((Vertice)tempArraySearch[i]).ID;
                    i = tempArraySearch.Length + 1;
                }
            }

            return id;
        }

        public Vertice getByIDVertice(int id)
        {
            Vertice returnVer = null;
            var tempArraySearch = listaVertices.toArray();

            for (int i = 0; i < tempArraySearch.Length; i++)
            {
                if (((Vertice)tempArraySearch[i]).ID == id)
                {
                    returnVer = (Vertice)tempArraySearch[i];
                    i = tempArraySearch.Length + 1;
                }
            }

            return returnVer;
        }

        public Lista getAdjacentVertices(int id)
        {
            Lista returnAdjacent = null;
            var tempArraySearch = listaVertices.toArray();

            if (id != -1)
            {
                for (int i = 0; i < tempArraySearch.Length; i++)
                {
                    if (((Vertice)tempArraySearch[i]).ID == id)
                    {
                        returnAdjacent = ((Vertice)tempArraySearch[i]).getAdjacentVertices();
                        i = tempArraySearch.Length + 1;
                    }
                }
            }

            return returnAdjacent;
        }

        public int getEdgeGrado(int id)
        {
            var adjacent = getAdjacentVertices(id);
            return (adjacent != null) ? adjacent.size() : 0;
        }

        public int NumberVertices()
        {
            return listaVertices.size();
        }

        public string getAristaWeight(int ID)
        {
            string strBuilder = "";

            Node recorridoNode = listaArista.Head;

            while(recorridoNode != null) 
            {
                if (((Arista)recorridoNode.Objeto).V1.ID == ID && ((Arista)recorridoNode.Objeto).V1.ID == ID)
                {
                    strBuilder += "IDv1: " + ((Arista)recorridoNode.Objeto).V1.ID + " IDv2: " + ((Arista)recorridoNode.Objeto).V1.ID + " Adj: " + "Peso: " + ((Arista)recorridoNode.Objeto).Weight + "\n";
                }
                recorridoNode = recorridoNode.Next;
            }

            return strBuilder;
        }

        public override string ToString()
        {
            string strBuilder = "";

            Node recorridoNode = listaVertices.Head;
            while(recorridoNode != null) 
            {
                strBuilder += "ID: " + ((Vertice)recorridoNode.Objeto).ID + " Dato: " + ((Vertice)recorridoNode.Objeto).Dato + " Adj: " + ((Vertice)recorridoNode.Objeto).getAdjacentVertices() + "\n";
                recorridoNode = recorridoNode.Next;
            }

            return strBuilder;
        }
    }
}
