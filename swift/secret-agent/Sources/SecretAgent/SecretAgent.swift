let SECRET_PASSCODE = "5up3r53cr37";
let BAD_PASSWORD_MESSAGE = "Sorry. No hidden secrets here.";

func protectSecret(_ secret: String, withPassword password: String) -> (String) -> String {
    func getSecret(withPassword password: String) -> String {
        if (password == SECRET_PASSCODE) {
            return secret;
        } else {
            return BAD_PASSWORD_MESSAGE;
        }
    }
    return getSecret;
}

func generateCombination(forRoom room: Int, usingFunction f: (Int) -> Int) -> (Int, Int, Int) {
   func generate() -> (Int, Int, Int) {
        var val1 = f(room: room Int);
        var val2 = f(arg1: val1 Int);
        var val3 = f(arg2: val2 Int);
        return (val1, val2, val3);
   }
   return generate;
}
