package project;
import java.util.ArrayList;
import java.util.Date;

class CamiloSyncAlgorithm implements SyncAlgorithm {
    
    public CamiloSyncAlgorithm(){} 
    
    public void Syncronized(ArrayList<Machine> listamaquinas){
        ServerTime serverhora = new ServerTime();
        Date hora = serverhora.GetTime();
        listamaquinas.forEach((m) -> { m.setTime( hora ); } );
    }
}