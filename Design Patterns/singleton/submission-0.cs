public class Singleton {

    private static Singleton _instance =  null;
    private string _value = null;
    private Singleton() {
      
    }

    public static Singleton getInstance() {
        if (_instance == null){
            _instance = new Singleton();
        }
        return _instance;
    }

    public string getValue() {
        return _value;
    }

    public void setValue(string value){
        _value = value;
    }
}
