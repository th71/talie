from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

def extrait_segment(parametres) :
        from lxml import etree
        import os
        print "-- FONCTION EXTRACTION : REPERTOIRE"
        fch = os.listdir('..')
        for i in fch :
                print i
        
        print "-- FONCTION EXTRACTION : params %s" % parametres
        if (parametres.has_key('fichier')):
                nom_fichier = parametres['fichier']
                chemin_fichier = '../xml2/%s' % nom_fichier
                fichier = open(chemin_fichier,'r')
                code_xml = fichier.read()

        if (parametres.has_key('id')):
                id_elem = parametres['id']
                arbre = etree.fromstring(code_xml)
                
                expression_xpath ='/tei:TEI//*[@xml:id="%s"]' % id_elem
                nsl ={'tei':'http://www.tei-c.org/ns/1.0'}
                
                segment = arbre.xpath(expression_xpath, namespaces=nsl)
                
                reponse = etree.tostring(segment[0],pretty_print=True)
        else :
                reponse = code_xml

        return reponse

def base_de_liens(urn) :
        base = {u'Virgilius.xml#L3.C1':u'LaCerda-LA.xml#L3.C1.A',
                u'Virgilius.xml#L3.C1.Sa':u'LaCerda-LA.xml#L3.C1.E.a',
                u'Virgilius.xml#L3.C1.Sb':u'LaCerda-LA.xml#L3.C1.E.b',
                u'Virgilius.xml#L3.C1.Sc':u'LaCerda-LA.xml#L3.C1.E.c',
                u'Virgilius.xml#L3.C1.Sd':u'LaCerda-LA.xml#L3.C1.E.d',
                u'Virgilius.xml#L3.w4':u'LaCerda-LA.xml#L3.C1.N.1',
        }
        if base.has_key(urn) :
                return base[urn]
        else:
                return None

# Create your views here.
def load(request) :
        print "-- FONCTION LOAD --"
        return HttpResponse( extrait_segment(request.GET) )

def loadHTML(request) :
        print "-- FONCTION LOAD HTML --"


        xml = extrait_segment (request.GET)
        print xml
        context = { 'xml' : xml ,
        }
        return render(request,'load/vide.html',context)

def associations(request) :
        from lxml import etree
        fichier = request.GET['fichier']

        xml = extrait_segment (request.GET)
        arbre=etree.fromstring(xml)

        expression_xpath = '//*[@xml:id]'
        nsl ={'tei':'http://www.tei-c.org/ns/1.0'}
        segments = arbre.xpath(expression_xpath, namespaces=nsl)

        print "RECHERCHE DES ASSOCIATIONS"
        for seg in segments :
                idSeg = seg.xpath('@xml:id', namespaces=nsl)[0]
                idSeg = fichier+"#"+idSeg
                print "ASSOCIATION PAR BASE DE LIEN"
                idSegLie = base_de_liens(idSeg)
                print "%s --> %s" % (idSeg, idSegLie)
                print "==",idSeg
                if (idSegLie<>None) :
                        print " ----> suivi"
                        (fichier_lie,id_lie) = idSegLie.split('#')
                        param_lien={'fichier':fichier_lie,'id':id_lie}
                        xml +=  ("%s --> %s <br/>" % (idSeg,idSegLie))
                        xml +=  extrait_segment (param_lien)

        context={ 'xml': xml }
        return render(request,"load/ancien.html", context)
