# Single source of truth for the DevSecOps CV (EN + FR).
C = {}

C["en"] = dict(
    lang="en",
    title="DevSecOps &amp; Cloud Security Engineering Student",
    avail="End-of-Studies Internship (PFE) · available January 2027",
    location="Tunisia",
    langs_short="English (bilingual) · French (bilingual)",
    h=dict(profile="Profile", edu="Education", skills="Technical Skills", exp="Experience",
           proj="Projects", certs="Certifications", comm="Security Community", langs="Languages",
           highlights="Security Highlights"),
    profile=("Cybersecurity &amp; Cloud Computing engineering student (top of class), building security into the software lifecycle. I harden Spring Boot back ends against the "
             "<b>OWASP Top 10</b>, automate delivery with <b>CI/CD</b> and secrets management, and run workloads on "
             "<b>Docker, Kubernetes and hybrid cloud (OpenStack + AWS)</b> behind segmented networks monitored by a "
             "<b>Wazuh SIEM</b>, with controls aligned to <b>ISO/IEC 27001:2022</b>. Securinets member and CTF player."),
    profile_short=("Cybersecurity &amp; Cloud Computing engineering student (top of class) who builds security into the software lifecycle: "
                   "OWASP-hardened Spring Boot back ends, CI/CD with secrets management, Docker/Kubernetes on hybrid cloud, segmented networks and SIEM monitoring, "
                   "with controls aligned to ISO/IEC 27001:2022. Securinets member and CTF player."),
    edu=[("ESPRIM Monastir", "Engineering Degree, Cybersecurity &amp; Cloud Computing", "2024 – 2027", "Top of class"),
         ("ISIMa Mahdia", "BSc, Software Engineering", "2021 – 2024", "Highest honours")],
    skills=[
        ("AppSec &amp; Standards", "OWASP Top 10, ISO/IEC 27001:2022 (Annex A), secure coding, Spring Security, JWT, OAuth2, OpenID Connect, BCrypt, RBAC / least privilege, input validation, audit logging"),
        ("CI/CD &amp; Automation", "GitHub Actions, GitLab CI/CD, secrets management (GitHub Secrets, SSH keys), Bash scripting, Git"),
        ("Containers &amp; Cloud", "Docker, Kubernetes, Nginx, AWS (EC2), OpenStack private cloud, hybrid cloud deployment"),
        ("Identity &amp; Access (IAM)", "Keycloak (SSO, OIDC), Active Directory, Kerberos"),
        ("Network Security", "pfSense firewalls, DMZ, network segmentation, bastion host, Cisco / Nexus switching &amp; routing, VLANs, DNS/DHCP, GNS3"),
        ("Monitoring &amp; SIEM", "Wazuh (agents, centralized log collection), Grafana, Prometheus, Loki, Wireshark"),
        ("Languages &amp; Stack", "Java, Python, Bash, JavaScript/TypeScript, SQL · Spring Boot, FastAPI, Node.js, Angular, React · PostgreSQL, MySQL, MongoDB, Kafka · Ubuntu, Kali Linux, Windows Server"),
    ],
    highlights=[
        ("4 / 10", "OWASP Top 10 risks mitigated in an ERP: A01, A03, A07, A09"),
        ("5 zones", "segmented network: DMZ, admin, front, back, DB, plus bastion host"),
        ("100%", "of hosts shipping logs to a centralized Wazuh SIEM"),
        ("0 manual", "steps: GitHub Actions build and deploy to AWS"),
    ],
    jobs=[
        dict(title="Software Engineering Intern, Secure Back-End (ERP)", org="Polymaille (Textile Industry)",
             place="Ksar Hellal, Tunisia", when="Jul – Sep 2026", bullets=[
            "<b>Built a full-cycle ERP replacing a legacy system</b> as a Spring Boot Modulith with 4 business modules (purchase, stock, production, sales): supplier orders, approval workflow, delivery notes, invoices and payments; each module scoped with the business lead and validated with users.",
            "<b>Implemented authentication and authorization with Spring Security:</b> stateless JWT filter, BCrypt password hashing and 5 roles enforced by method-level RBAC (@PreAuthorize) under least privilege, addressing OWASP A01 (Broken Access Control) and A07 (Authentication Failures); aligned with ISO 27001 A.5.15 / A.8.5.",
            "<b>Prevented injection (OWASP A03)</b> with Bean Validation and parameterized JPA queries, and <b>built a persistent audit trail</b> (who approved what, and when) on orders, invoices and payments for traceability and non-repudiation (OWASP A09, ISO 27001 A.8.15).",
        ]),
        dict(title="Full-Stack / Backend Developer (3 internships)", org="Alfa Computers",
             place="Mahdia, Tunisia", when="Mar 2024 – Aug 2025", bullets=[
            "<b>Built \"The Hive\" trading platform backend</b> with fully authenticated REST endpoints (FastAPI, JWT + OAuth2), documented in OpenAPI/Swagger and covered by Postman test suites.",
            "<b>Delivered a MERN e-commerce platform solo</b>, containerized with Docker and auto-deployed through GitLab CI/CD to Render; <b>led a 3-person team</b> shipping an IoT smart-home app.",
        ]),
    ],
    projects=[
        dict(name="Secured Banking Infrastructure", sub="team of 6", when="2026",
             stack="GNS3 · Cisco Nexus · pfSense · Wazuh · Keycloak · OpenStack · AWS · GitHub Actions · Spring Boot · Kafka", bullets=[
            "<b>Designed a defense-in-depth network in GNS3 with 5 security zones</b> (DMZ, administration, front-end, back-end, database): Cisco Nexus switches, routers, pfSense firewalls, bastion host for admin access, Nginx reverse proxy, DNS/DHCP (ISO 27001 A.8.20 / A.8.22).",
            "<b>Deployed a centralized SIEM:</b> a Wazuh agent on every host, with logs forwarded through a collector to the central manager (ISO 27001 A.8.15 / A.8.16).",
            "<b>Automated deployment with GitHub Actions</b> to a hybrid cloud (OpenStack in GNS3 + AWS): the pipeline builds the Spring Boot JAR, pulled by the AWS VM over SSH with keys kept in GitHub Secrets; no manual deploy steps left.",
            "<b>Owned the KYC module</b> of a 7-microservice banking app (database per service, Kafka eventing) secured with Keycloak SSO (OpenID Connect) and RBAC. <b>Nominated, ESPRIT Projects Ball.</b>",
        ]),
        dict(name="Hermes Suite, E-commerce Platform (MERN)", sub="", when="2024 – present",
             stack="React · Node.js · MongoDB Atlas · Docker · Render", text=
            "JWT-secured e-commerce (catalogue, cart, orders, PDF invoices), evolving into a multi-tenant SaaS."),
        dict(name="Windows Server &amp; Network Services Lab", sub="", when="2026",
             stack="Windows Server · Active Directory · Kerberos", text=
            "FTP, DNS and DHCP roles with Kerberos authentication and granular file permissions."),
    ],
    certs="CLLMSP &amp; CRTOM (Red Team Leaders, 2026) · Cisco CCNA 200-301 (in progress) · Full-Stack MERN (100h) · Building AI Agents (DeepLearning.AI)",
    community=[
        "Member of <b>Securinets</b>; CTF player on TryHackMe, picoCTF and Tunisian CTFs. Co-founded <b>Hunters Club</b> (20+ members): 2nd &amp; 4th place at Polytech Sousse CTF; ambassador, CyberSphere Congress (7th ed.).",
        "Led the Cyber &amp; Cloud committee at <b>DevTalents</b> (30+ members) · <b>2nd place</b>, Clean &amp; Green hackathon 2025.",
    ],
    languages="<b>Arabic</b> native · <b>French</b> bilingual · <b>English</b> bilingual · <b>German</b> basic",
)

C["fr"] = dict(
    lang="fr",
    title="Élève ingénieur DevSecOps &amp; Sécurité Cloud",
    avail="Stage de fin d'études (PFE) · disponible dès janvier 2027",
    location="Tunisie",
    langs_short="Français (bilingue) · Anglais (bilingue)",
    h=dict(profile="Profil", edu="Formation", skills="Compétences techniques", exp="Expérience professionnelle",
           proj="Projets", certs="Certifications", comm="Communauté sécurité", langs="Langues",
           highlights="Chiffres clés sécurité"),
    profile=("Élève ingénieur en Cybersécurité &amp; Cloud Computing (major de promotion), j'intègre la sécurité tout au long du cycle de vie logiciel. Je sécurise des back-ends Spring Boot contre l'<b>OWASP Top 10</b>, "
             "j'automatise la livraison en <b>CI/CD</b> avec gestion des secrets, et je déploie sur <b>Docker, Kubernetes et cloud "
             "hybride (OpenStack + AWS)</b> derrière des réseaux segmentés supervisés par un <b>SIEM Wazuh</b>, avec des contrôles "
             "alignés sur l'<b>ISO/IEC 27001:2022</b>. Membre de Securinets et joueur de CTF."),
    profile_short=("Élève ingénieur en Cybersécurité &amp; Cloud Computing (major de promotion), j'intègre la sécurité dans tout le cycle de vie logiciel : "
                   "back-ends Spring Boot durcis contre l'OWASP Top 10, CI/CD avec gestion des secrets, Docker/Kubernetes sur cloud hybride, réseaux segmentés et supervision SIEM, "
                   "avec des contrôles alignés sur l'ISO/IEC 27001:2022. Membre de Securinets et joueur de CTF."),
    edu=[("ESPRIM Monastir", "Cycle ingénieur, Cybersécurité &amp; Cloud Computing", "2024 – 2027", "Major de promotion"),
         ("ISIMa Mahdia", "Licence en génie logiciel", "2021 – 2024", "Félicitations du jury")],
    skills=[
        ("AppSec &amp; normes", "OWASP Top 10, ISO/IEC 27001:2022 (Annexe A), développement sécurisé, Spring Security, JWT, OAuth2, OpenID Connect, BCrypt, RBAC / moindre privilège, validation des entrées, audit logging"),
        ("CI/CD &amp; automatisation", "GitHub Actions, GitLab CI/CD, gestion des secrets (GitHub Secrets, clés SSH), scripts Bash, Git"),
        ("Conteneurs &amp; cloud", "Docker, Kubernetes, Nginx, AWS (EC2), cloud privé OpenStack, déploiement cloud hybride"),
        ("Identités &amp; accès (IAM)", "Keycloak (SSO, OIDC), Active Directory, Kerberos"),
        ("Sécurité réseau", "pare-feux pfSense, DMZ, segmentation réseau, bastion, commutation et routage Cisco / Nexus, VLAN, DNS/DHCP, GNS3"),
        ("Supervision &amp; SIEM", "Wazuh (agents, collecte centralisée des logs), Grafana, Prometheus, Loki, Wireshark"),
        ("Langages &amp; stack", "Java, Python, Bash, JavaScript/TypeScript, SQL · Spring Boot, FastAPI, Node.js, Angular, React · PostgreSQL, MySQL, MongoDB, Kafka · Ubuntu, Kali Linux, Windows Server"),
    ],
    highlights=[
        ("4 / 10", "risques OWASP Top 10 traités dans un ERP : A01, A03, A07, A09"),
        ("5 zones", "réseau segmenté : DMZ, admin, front, back, BDD, plus bastion"),
        ("100 %", "des machines remontent leurs logs vers un SIEM Wazuh centralisé"),
        ("0 étape", "manuelle : build et déploiement GitHub Actions vers AWS"),
    ],
    jobs=[
        dict(title="Stagiaire ingénieur logiciel, back-end sécurisé (ERP)", org="Polymaille (industrie textile)",
             place="Ksar Hellal, Tunisie", when="juil. – sept. 2026", bullets=[
            "<b>ERP complet remplaçant un système existant</b>, en Spring Boot Modulith avec 4 modules métier (achats, stock, production, ventes) : commandes fournisseurs, circuit de validation, bons de livraison, factures et paiements ; modules cadrés avec le métier et validés par les utilisateurs.",
            "<b>Authentification et autorisation avec Spring Security :</b> filtre JWT stateless, hachage BCrypt et 5 rôles appliqués par RBAC au niveau des méthodes (@PreAuthorize) selon le moindre privilège, contre OWASP A01 (contrôle d'accès défaillant) et A07 (défauts d'authentification) ; aligné ISO 27001 A.5.15 / A.8.5.",
            "<b>Prévention des injections (OWASP A03)</b> par Bean Validation et requêtes JPA paramétrées, et <b>piste d'audit persistée</b> (qui a validé quoi, et quand) sur commandes, factures et paiements pour la traçabilité et la non-répudiation (OWASP A09, ISO 27001 A.8.15).",
        ]),
        dict(title="Développeur Full-Stack / Back-end (3 stages)", org="Alfa Computers",
             place="Mahdia, Tunisie", when="mars 2024 – août 2025", bullets=[
            "<b>Back-end de la plateforme de trading « The Hive »</b> avec endpoints REST entièrement authentifiés (FastAPI, JWT + OAuth2), documentés en OpenAPI/Swagger et testés avec Postman.",
            "<b>Plateforme e-commerce MERN réalisée seul</b>, conteneurisée avec Docker et déployée automatiquement via GitLab CI/CD vers Render ; <b>encadrement d'une équipe de 3</b> sur une application domotique IoT.",
        ]),
    ],
    projects=[
        dict(name="Infrastructure bancaire sécurisée", sub="équipe de 6", when="2026",
             stack="GNS3 · Cisco Nexus · pfSense · Wazuh · Keycloak · OpenStack · AWS · GitHub Actions · Spring Boot · Kafka", bullets=[
            "<b>Conception d'un réseau en défense en profondeur sous GNS3 avec 5 zones de sécurité</b> (DMZ, administration, front-end, back-end, base de données) : switchs Cisco Nexus, routeurs, pare-feux pfSense, bastion d'administration, reverse proxy Nginx, DNS/DHCP (ISO 27001 A.8.20 / A.8.22).",
            "<b>Déploiement d'un SIEM centralisé :</b> un agent Wazuh sur chaque machine, logs remontés via un collecteur vers le serveur central (ISO 27001 A.8.15 / A.8.16).",
            "<b>Automatisation du déploiement avec GitHub Actions</b> vers un cloud hybride (OpenStack dans GNS3 + AWS) : le pipeline compile le JAR Spring Boot, récupéré en SSH par la VM AWS avec des clés dans GitHub Secrets ; plus aucune étape manuelle.",
            "<b>Responsable du module KYC</b> d'une application bancaire de 7 microservices (une base par service, événements Kafka) sécurisée par Keycloak SSO (OpenID Connect) et RBAC. <b>Nominé, ESPRIT Projects Ball.</b>",
        ]),
        dict(name="Hermes Suite, plateforme e-commerce (MERN)", sub="", when="2024 – aujourd'hui",
             stack="React · Node.js · MongoDB Atlas · Docker · Render", text=
            "E-commerce sécurisé par JWT (catalogue, panier, commandes, factures PDF), en évolution vers un SaaS multi-tenant."),
        dict(name="Lab Windows Server &amp; services réseau", sub="", when="2026",
             stack="Windows Server · Active Directory · Kerberos", text=
            "Rôles FTP, DNS et DHCP avec authentification Kerberos et permissions de fichiers granulaires."),
    ],
    certs="CLLMSP &amp; CRTOM (Red Team Leaders, 2026) · Cisco CCNA 200-301 (en cours) · Full-Stack MERN (100 h) · Building AI Agents (DeepLearning.AI)",
    community=[
        "Membre de <b>Securinets</b> ; CTF sur TryHackMe, picoCTF et compétitions tunisiennes. Cofondateur du <b>Hunters Club</b> (20+ membres) : 2e et 4e places au CTF Polytech Sousse ; ambassadeur du CyberSphere Congress (7e éd.).",
        "Responsable du comité Cyber &amp; Cloud chez <b>DevTalents</b> (30+ membres) · <b>2e place</b>, hackathon Clean &amp; Green 2025.",
    ],
    languages="<b>Arabe</b> maternelle · <b>Français</b> bilingue · <b>Anglais</b> bilingue · <b>Allemand</b> notions",
)
