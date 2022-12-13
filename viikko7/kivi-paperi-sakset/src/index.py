from tehdas import Tehdas


def main():
    while True:
        pelit = {
            "a": Tehdas.luo_kps_pelaaja_vs_pelaaja(),
            "b": Tehdas.luo_kps_pelaaja_vs_tekoaly(),
            "c": Tehdas.luo_kps_pelaaja_vs_parempi_tekoaly(10)
        }
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )

        vastaus = input()
        if vastaus in ["a", "b", "c"]:
            print(
                "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
            )
            peli = pelit[vastaus]
            peli.pelaa()
        else:
            break


if __name__ == "__main__":
    main()
