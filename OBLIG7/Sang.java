public class Sang{
    String tittel;
    String navn;

    public Sang(String tittel, String navn){
        this.tittel = tittel;
        this.navn = navn;
    }

    private boolean sjekkArtisn(String navn){
        String navngammel[] = this.navn.split(" ");
        String navnny[] = navn.split(" ");
        for (String i : navnny){
            for (String j : navngammel){
                if (i.lower() == j.lower()){
                    return true;
                }
                else{
                    return false;
                }
            }
        }
    }

    private boolean sjekkTittel(String nyTittel){
        if(this.tittel.lower() == nyTittel.lower()){
            return true;
        }
        else{
            return false;
        }
    }

    private boolean sjekkArtistogTittel(String artist, String tittel){
        if(navn.lower() == artist.lower() && this.tittel.lower() == tittel.lower){
            return true;
        }
        else{
            return false;
        }
    }
}