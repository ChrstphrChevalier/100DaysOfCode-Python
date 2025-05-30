import argparse
from password_generator import generate_password
from crypto import encrypt_data, decrypt_data
from keyring_manager import save_password, get_password, delete_password

def main():
    parser = argparse.ArgumentParser(description="🔐 Gestionnaire de mots de passe CLI")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # generate
    gen_parser = subparsers.add_parser("generate", help="Génère, chiffre et stocke un mot de passe")
    gen_parser.add_argument("--service", required=True, help="Nom du service (ex : github.com)")
    gen_parser.add_argument("--username", required=True, help="Identifiant utilisateur")
    gen_parser.add_argument("--length", type=int, default=16, help="Longueur du mot de passe (défaut : 16)")

    # get
    get_parser = subparsers.add_parser("get", help="Récupère et déchiffre un mot de passe")
    get_parser.add_argument("--service", required=True)
    get_parser.add_argument("--username", required=True)

    # delete
    del_parser = subparsers.add_parser("delete", help="Supprime un mot de passe du keyring")
    del_parser.add_argument("--service", required=True)
    del_parser.add_argument("--username", required=True)

    args = parser.parse_args()

    if args.command == "generate":
        pwd = generate_password(args.length)
        token = encrypt_data(pwd)
        save_password(args.service, args.username, token)
        print(f"✅ Mot de passe généré et stocké pour {args.service}/{args.username}")

    elif args.command == "get":
        token = get_password(args.service, args.username)
        if token:
            try:
                pwd = decrypt_data(token)
                print(f"🔓 Mot de passe pour {args.service}/{args.username} : {pwd}")
            except Exception:
                print("❌ Erreur : impossible de déchiffrer le mot de passe.")
        else:
            print("❌ Aucun mot de passe trouvé.")

    elif args.command == "delete":
        try:
            delete_password(args.service, args.username)
            print(f"🗑️ Mot de passe supprimé pour {args.service}/{args.username}")
        except Exception:
            print("❌ Erreur : rien à supprimer.")

if __name__ == "__main__":
    main()
