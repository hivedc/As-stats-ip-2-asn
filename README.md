# Convert ip2asn.tsv to ip2asn.json

Petit script qui télécharge la version la plus récente de la liste mappée  du site [ip2asn](https://iptoasn.com/)

Avant la première exécution, il faut s'assurer que les dépendance soient installées.
Pour se faire, python doit être en version >= 3.0 et on exécute en ligne de commande à partir du dossier où le script a été extrait:
> **pip** install -r requirements.txt

Pour utiliser le script, on lui donne les droits d'éxécutions
> **sudo chmod +x** ./ip_json_creator.py

Puis pour exécuter:
> **python3** ./ip_json_creator.py --name LeNomDuFichier --of ./emplacement
