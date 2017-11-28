from lxml import etree

import sys
sys.path.insert(0,'/root/talie/talie')

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "talie.settings")

import django
django.setup()

from interface1.models import Associations

import glob
for nom_fichier in glob.glob('../../talie/xml/*.xml') :
    print nom_fichier
    
    fichier = open(nom_fichier,"r")

    virgilius = fichier.read()

    arbre = etree.fromstring(virgilius)

    extraction = arbre.xpath('//*[@xml:base|@xml:id]', namespaces={'tei':'http://www.tei-c.org/ns/1.0'})
    print len(extraction)

    for row in extraction :
        print etree.tostring(row,pretty_print=True)[0:500]
        print "===",row.xpath('@xml:base')
        URN=""
        for xbase in row.xpath('ancestor-or-self::*/@xml:base') :
            URN+=xbase
            print URN
            
            print "===INSERTION==="
            entree=Associations(origine=URN,
                                type_asso='ressource',
                                sous_type_asso='TEI',
                                destination=etree.tostring(row,pretty_print=True)
            )
            entree.save()
    
