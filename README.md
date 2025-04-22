# Contract Management - Odoo Technical Training Project

Ce projet a été réalisé dans le cadre de la formation **Odoo Technique**, visant à acquérir une maîtrise pratique du développement de modules personnalisés dans Odoo.

## 📦 Objectif du projet

Le but de ce module est de mettre en place une gestion simplifiée des contrats clients au sein d'Odoo. Ce module permet de :

- Créer et gérer des contrats liés à des partenaires.
- Définir des dates de début et de fin de contrat.
- Ajouter des conditions spécifiques ou des lignes de contrat (produits, services, etc.).
- Suivre l'état des contrats (brouillon, en cours, expiré).
- Intégrer des actions automatiques ou des rappels (via serveur d'action ou CRON, selon les fonctionnalités ajoutées).

## 🛠️ Fonctionnalités techniques

- Création d'un modèle `contract.contract` personnalisé.
- Utilisation de champs relationnels (`Many2one`, `One2many`, `Many2many`).
- Ajout de menus, actions et vues personnalisées (formulaire, liste).
- Sécurisation des accès avec des groupes et des règles d’enregistrement.
- Personnalisation de la vue avec Studio ou XML.

## 🚀 À propos de la formation

La **formation Odoo Technique** est conçue pour les développeurs souhaitant apprendre à :
- Créer des modules Odoo from scratch.
- Comprendre l’architecture MVC d’Odoo.
- Manipuler les vues, les modèles, et la logique serveur.
- Travailler avec les règles d’accès, les actions serveur, les rapports, et les automatisations.

---

## 📂 Structure du module

contract_management/ ├── manifest.py ├── models/ │ └── contract.py ├── views/ │ └── contract_views.xml ├── security/ │ ├── ir.model.access.csv │ 
└── security.xml └── README.md



---

## ✅ Pré-requis

- Odoo 16+ (Community ou Enterprise)
- Accès administrateur au backend Odoo
- Installation du module via Apps ou interface développeur

---

## 📧 Contact

Auteur : BOUZRBAY Ghita  
Formation : https://technapscompany.com/formation-odoo-technique  
GitHub : [https://github.com/ghbouzrbay](https://github.com/ghbouzrbay)


