import xml.etree.ElementTree as ET
import csv

def parse_permissions(filename):
    permission_names = []
    try:
        with open(filename, "r") as permissions_file:
            for line in permissions_file:
                permission_names.append(line[31:-4:])

        return permission_names
    except:
        return permission_names

def parse_manifest(filename, badPerm):
    manifest_tree = ET.parse(filename)
    manifest_root = manifest_tree.getroot()
    base_group = "Nada"
    permisosUsuario = [
        ("appperm.permission.TEST_PERMISSION1", "Dangerous"),
        ("appperm.permission.TEST1", "Normal"),
        ("appperm.permission.TEST2", "Normal"),
        ("appperm.permission.TEST3", "Signature"),
        ("appperm.permission.TEST4", "Signature"),
        ("appperm.permission.TEST5", "Dangerous"),
    ]
    permission_groups = {
        "appperm.permission-group.TEST_GROUP": [
            ("appperm.permission.TEST_PERMISSION2", "Normal")
        ],
        "appperm.permission-group.TEST_GROUP1": [
            ("appperm.permission.TEST_PERMISSION3", "Signature")
        ],
        base_group: permisosUsuario,
    }

    for element in manifest_root:
        element_name = element.tag
        if element_name == "permission-group":
            permission_group_name = element.attrib[
                "{http://schemas.android.com/apk/res/android}name"
            ]
            permission_groups[permission_group_name] = []
        elif element_name == "permission":
            permission_name = element.attrib[
                "{http://schemas.android.com/apk/res/android}name"
            ]
            if permission_name in badPerm:
                continue
            permission_protection_level = element.attrib[
                "{http://schemas.android.com/apk/res/android}protectionLevel"
            ]

            if "normal" in permission_protection_level:
                permission_tuple = (permission_name, "Normal")
                permission_groups[base_group].append(permission_tuple)
            elif "signature" in permission_protection_level:
                if "privileged" in permission_protection_level:
                    continue
                permission_tuple = (permission_name, "Signature")
                permission_groups[base_group].append(permission_tuple)
            elif "dangerous" in permission_protection_level:
                permission_tuple = (permission_name, "Dangerous")
                permission_groups[permission_group_name].append(permission_tuple)
    return permission_groups

def save_to_csv(permissions_dict, filename):
    with open(filename, "w", newline="") as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=";")
        csvwriter.writerow(["Permiso", "Grupo", "Protection"])

        for permission_group_name, permissions in permissions_dict.items():
            for permission_tuple in permissions:
                permission_name = permission_tuple[0]
                protection_level = permission_tuple[1]
                if permission_group_name == "Nada":
                    csvwriter.writerow([permission_name, "", protection_level])
                else:
                    csvwriter.writerow(
                        [permission_name, permission_group_name, protection_level]
                    )


def save_to_file(permissions_dict, filename):
    with open(filename, "w", encoding="utf-8") as permissions_file:
        for permission_group_name, permissions in permissions_dict.items():
            for permission_tuple in permissions:
                permission_name = permission_tuple[0]
                permissions_file.write(
                    '<uses-permission android:name="' + permission_name + '"/>\n'
                )

def print_permissions(permissions_dict):
    for permission_group_name, permissions in permissions_dict.items():
        print(permission_group_name + ":")
        for permission_tuple in permissions:
            print("  ", permission_tuple[0], ",", permission_tuple[1])

def main():
    filename = "AndroidManifestGitHub.xml"
    permissions_names = parse_permissions("malos.xml")
    permissions_dict = parse_manifest(filename, permissions_names)
    save_to_file(permissions_dict, "permisosManifest.txt")
    save_to_csv(permissions_dict, "Permisos.csv")

if __name__ == "__main__":
    main()