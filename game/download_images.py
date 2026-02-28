#!/usr/bin/env python3
"""
Download plant images from Wikimedia Commons via the Wikipedia API.
Uses the main image from each species' Wikipedia article.
"""

import json
import os
import sys
import time
import urllib.request
import urllib.parse
import urllib.error

DEST_DIR = os.path.join(os.path.dirname(__file__), "public", "images")

# (file_id, french_name, latin_name)
PLANTS = [
    # Tier 1
    ("jacinthe_des_bois", "Jacinthe des bois", "Hyacinthoides non-scripta"),
    ("ortie_dioique", "Ortie dioique", "Urtica dioica"),
    ("alliaire_officinale", "Alliaire officinale", "Alliaria petiolata"),
    ("listere_ovale", "Listere ovale", "Neottia ovata"),
    ("sceau_de_salomon", "Sceau de Salomon multiflore", "Polygonatum multiflorum"),
    ("lamier_jaune", "Lamier jaune", "Lamium galeobdolon"),
    ("lamier_tachete", "Lamier tachete", "Lamium maculatum"),
    # Tier 2
    ("herbe_a_robert", "Herbe a Robert", "Geranium robertianum"),
    ("benoite_urbaine", "Benoite urbaine", "Geum urbanum"),
    ("pulmonaire_officinale", "Pulmonaire officinale", "Pulmonaria officinalis"),
    ("gaillet_gratteron", "Gaillet gratteron", "Galium aparine"),
    ("scrofulaire_noueuse", "Scrofulaire noueuse", "Scrophularia nodosa"),
    ("circee_de_paris", "Circee de Paris", "Circaea lutetiana"),
    ("tussilage", "Tussilage pas-d'ane", "Tussilago farfara"),
    ("muguet", "Muguet", "Convallaria majalis"),
    ("neottie_nid_d_oiseau", "Neottie nid d'oiseau", "Neottia nidus-avis"),
    ("sanicle_d_europe", "Sanicle d'Europe", "Sanicula europaea"),
    ("adoxe_musquee", "Adoxe musquee", "Adoxa moschatellina"),
    ("sureau_noir", "Sureau noir", "Sambucus nigra"),
    # Tier 3
    ("berce_spondyle", "Berce spondyle", "Heracleum sphondylium"),
    ("angelique_des_bois", "Angelique des bois", "Angelica sylvestris"),
    ("epiaire_des_bois", "Epiaire des bois", "Stachys sylvatica"),
    ("renoncule_rampante", "Renoncule rampante", "Ranunculus repens"),
    ("fraisier_des_bois", "Fraisier des bois", "Fragaria vesca"),
    ("reine_des_pres", "Reine des pres", "Filipendula ulmaria"),
    ("valeriane_officinale", "Valeriane officinale", "Valeriana officinalis"),
    ("silene_dioique", "Silene dioique", "Silene dioica"),
    ("millepertuis", "Millepertuis perfore", "Hypericum perforatum"),
    ("consoude_officinale", "Consoude officinale", "Symphytum officinale"),
    ("primevere_elatior", "Primevere elevee", "Primula elatior"),
    ("violette_des_bois", "Violette des bois", "Viola reichenbachiana"),
    ("vesce_des_haies", "Vesce des haies", "Vicia sepium"),
    ("oxalis_des_bois", "Oxalis des bois", "Oxalis acetosella"),
    ("oseille_sanguine", "Oseille sanguine", "Rumex sanguineus"),
    ("liseron_des_haies", "Liseron des haies", "Calystegia sepium"),
    ("houblon", "Houblon", "Humulus lupulus"),
    ("cornouiller_sanguin", "Cornouiller sanguin", "Cornus sanguinea"),
    ("viorne_lantane", "Viorne lantane", "Viburnum lantana"),
    ("chevrefeuille_des_bois", "Chevrefeuille des bois", "Lonicera periclymenum"),
    ("chevrefeuille_des_haies", "Chevrefeuille des haies", "Lonicera xylosteum"),
    ("fusain_d_europe", "Fusain d'Europe", "Euonymus europaeus"),
    ("fragon_petit_houx", "Fragon petit-houx", "Ruscus aculeatus"),
    ("clematite_des_haies", "Clematite des haies", "Clematis vitalba"),
    ("fritillaire_pintade", "Fritillaire pintade", "Fritillaria meleagris"),
    # Tier 4
    ("chicoree_sauvage", "Chicoree sauvage", "Cichorium intybus"),
    ("carotte_sauvage", "Carotte sauvage", "Daucus carota"),
    ("fumeterre_officinale", "Fumeterre officinale", "Fumaria officinalis"),
    ("moutarde_des_champs", "Moutarde des champs", "Sinapis arvensis"),
    ("sainfoin", "Sainfoin", "Onobrychis viciifolia"),
    ("sauge_des_pres", "Sauge des pres", "Salvia pratensis"),
    ("bleuet", "Bleuet", "Centaurea cyanus"),
    ("coquelicot", "Coquelicot", "Papaver rhoeas"),
    ("calament_officinal", "Calament officinal", "Clinopodium nepeta"),
    # New plants
    ("aubepine", "Aubepine", "Crataegus monogyna"),
    ("origan", "Origan", "Origanum vulgare"),
    ("lotier_cornicule", "Lotier cornicule", "Lotus corniculatus"),
    ("eglantier", "Eglantier", "Rosa canina"),
    ("prunellier", "Prunellier", "Prunus spinosa"),
    ("buis", "Buis", "Buxus sempervirens"),
    ("thym_serpolet", "Thym serpolet", "Thymus serpyllum"),
    ("orchis_pourpre", "Orchis pourpre", "Orchis purpurea"),
    ("centauree_jacee", "Centauree jacee", "Centaurea jacea"),
    ("knautie_des_champs", "Knautie des champs", "Knautia arvensis"),
    ("scabieuse_colombaire", "Scabieuse colombaire", "Scabiosa columbaria"),
    ("cardere_sauvage", "Cardere sauvage", "Dipsacus fullonum"),
    ("brunelle_commune", "Brunelle commune", "Prunella vulgaris"),
    ("ophrys_abeille", "Ophrys abeille", "Ophrys apifera"),
    ("heliantheme", "Heliantheme commun", "Helianthemum nummularium"),
    ("germandree", "Germandree petit-chene", "Teucrium chamaedrys"),
    ("bugrane_epineuse", "Bugrane epineuse", "Ononis spinosa"),
    ("anthyllide", "Anthyllide vulneraire", "Anthyllis vulneraria"),
    ("hippocrepide", "Hippocrepide en ombelle", "Hippocrepis comosa"),
    ("reseda_jaune", "Reseda jaune", "Reseda lutea"),
    ("pimprenelle", "Pimprenelle", "Sanguisorba minor"),
    ("globulaire", "Globulaire commune", "Globularia bisnagarica"),
    ("lin_purgatif", "Lin purgatif", "Linum catharticum"),
    ("euphraise", "Euphraise officinale", "Euphrasia officinalis"),
    ("genevrier", "Genevrier commun", "Juniperus communis"),
]

API_URL = "https://en.wikipedia.org/w/api.php"
COMMONS_API_URL = "https://commons.wikimedia.org/w/api.php"
USER_AGENT = "PlantGameImageDownloader/1.0 (educational project)"


def get_image_from_wikipedia(latin_name):
    """Try to get the main image from the English Wikipedia article."""
    params = urllib.parse.urlencode({
        "action": "query",
        "titles": latin_name,
        "prop": "pageimages",
        "piprop": "thumbnail",
        "pithumbsize": "1280",
        "format": "json",
        "redirects": "1",
    })
    url = f"{API_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
        for page in pages.values():
            thumb = page.get("thumbnail", {})
            if thumb.get("source"):
                return thumb["source"]
    except Exception as e:
        print(f"  Wikipedia API error: {e}")
    return None


def get_image_from_commons(latin_name):
    """Fallback: search Wikimedia Commons directly."""
    params = urllib.parse.urlencode({
        "action": "query",
        "generator": "search",
        "gsrnamespace": "6",
        "gsrsearch": latin_name,
        "gsrlimit": "5",
        "prop": "imageinfo",
        "iiprop": "url|mime",
        "iiurlwidth": "1280",
        "format": "json",
    })
    url = f"{COMMONS_API_URL}?{params}"
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = json.loads(resp.read().decode())
        pages = data.get("query", {}).get("pages", {})
        for page in sorted(pages.values(), key=lambda p: p.get("index", 999)):
            for info in page.get("imageinfo", []):
                mime = info.get("mime", "")
                if mime.startswith("image/") and "svg" not in mime:
                    return info.get("thumburl") or info.get("url")
    except Exception as e:
        print(f"  Commons API error: {e}")
    return None


def download_file(url, dest_path):
    """Download a file from URL to dest_path."""
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=30) as resp:
        with open(dest_path, "wb") as f:
            f.write(resp.read())


def main():
    os.makedirs(DEST_DIR, exist_ok=True)

    success = []
    failed = []

    for file_id, french_name, latin_name in PLANTS:
        # Check if already downloaded
        existing = [f for f in os.listdir(DEST_DIR) if f.startswith(file_id + ".")]
        if existing:
            print(f"[SKIP] {french_name} - already exists ({existing[0]})")
            success.append((file_id, french_name, latin_name, existing[0]))
            continue

        print(f"[DL]   {french_name} ({latin_name})...", end=" ", flush=True)

        # Try Wikipedia first, then Commons
        img_url = get_image_from_wikipedia(latin_name)
        if not img_url:
            img_url = get_image_from_commons(latin_name)

        if not img_url:
            print("FAILED - no image found")
            failed.append((file_id, french_name, latin_name))
            continue

        # Determine extension from URL
        url_path = urllib.parse.urlparse(img_url).path.lower()
        if ".png" in url_path:
            ext = "png"
        elif ".gif" in url_path:
            ext = "gif"
        else:
            ext = "jpg"

        filename = f"{file_id}.{ext}"
        dest_path = os.path.join(DEST_DIR, filename)

        try:
            download_file(img_url, dest_path)
            size_kb = os.path.getsize(dest_path) / 1024
            print(f"OK ({size_kb:.0f} KB) -> {filename}")
            success.append((file_id, french_name, latin_name, filename))
        except Exception as e:
            print(f"FAILED - {e}")
            failed.append((file_id, french_name, latin_name))

        # Be polite to the API
        time.sleep(10)

    print(f"\n{'='*60}")
    print(f"Done: {len(success)} downloaded, {len(failed)} failed")

    if failed:
        print(f"\nFailed plants:")
        for file_id, french_name, latin_name in failed:
            print(f"  - {french_name} ({latin_name})")

    # Output the plants.js entries for successful downloads
    if success:
        print(f"\n{'='*60}")
        print("plants.js entries to add:\n")
        for file_id, french_name, latin_name, filename in success:
            print(f"  {{ id: '{file_id}', name: '{french_name}', latin: '{latin_name}', image: '/images/{filename}' }},")


if __name__ == "__main__":
    main()
