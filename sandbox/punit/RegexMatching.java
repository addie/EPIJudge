package dp;

import java.util.Random;

public class RegexMatching {

	public boolean isMatch(String text, String pattern) {
        if (pattern.isEmpty()) return text.isEmpty();
        boolean first_match = (!text.isEmpty() && 
                               (pattern.charAt(0) == text.charAt(0) || pattern.charAt(0) == '.'));
        
        if (pattern.length() >= 2 && pattern.charAt(1) == '*'){
            return (isMatch(text, pattern.substring(2)) || 
                    (first_match && isMatch(text.substring(1), pattern)));
        } else {
            return first_match && isMatch(text.substring(1), pattern.substring(1));
        }
    }
 
    /**
     * Dynamic programming technique for regex matching.
     */
    public boolean matchRegex(char[] text, char[] pattern) {
        boolean T[][] = new boolean[text.length + 1][pattern.length + 1];

        T[0][0] = true;
        //Deals with patterns like a* or a*b* or a*b*c*
        for (int i = 1; i < T[0].length; i++) {
            if (pattern[i-1] == '*') {
                T[0][i] = T[0][i - 2];
            }
        }

        for (int i = 1; i < T.length; i++) {
            for (int j = 1; j < T[0].length; j++) {
                if (pattern[j - 1] == '.' || pattern[j - 1] == text[i - 1]) {
                    T[i][j] = T[i-1][j-1];
                } else if (pattern[j - 1] == '*')  {
                    T[i][j] = T[i][j - 2]; // no occurences
                    if (pattern[j-2] == '.' || pattern[j - 2] == text[i - 1]) {
                        T[i][j] = T[i][j] || T[i - 1][j]; // 1 or more occurences
                    }
                } else {
                    T[i][j] = false;
                }
            }
        }
        return T[text.length][pattern.length];
    }
    
    
    public boolean matchRegex1D(char[] text, char[] pattern) {
        boolean T[] = new boolean[pattern.length + 1];

        T[0] = true;
        //Deals with patterns like a* or a*b* or a*b*c*
        for (int i = 1; i < T.length; i++) {
            if (pattern[i-1] == '*') {
                T[i] = T[i - 2];
            }
        }

        for (int i = 1; i <= text.length; i++) {
        	boolean temp[] = new boolean[pattern.length+1];
            for (int j = 1; j <= pattern.length; j++) {
                if (pattern[j - 1] == '.' || pattern[j - 1] == text[i - 1]) {
                    temp[j] = T[j-1];
                } else if (pattern[j - 1] == '*')  {
                    temp[j] = temp[j - 2]; // no occurences
                    if (pattern[j-2] == '.' || pattern[j - 2] == text[i - 1]) {
                        temp[j] = temp[j] || T[j]; // 1 or more occurences
                    }
                } else {
                    temp[j] = false;
                }
            }
            T = temp;
        }
        return T[pattern.length];
    }
    
    public void generateTestCases() {
    	Random r = new Random();
    	StringBuilder text = new StringBuilder();
    	int length = r.nextInt(15)+1;
    	for (int i = 0; i < length; i++) {
    		int charValue = r.nextInt(26);    		
        	int character = 'a' + charValue;        
        	String t = Character.toString((char)character);
    		t = r.nextBoolean() ? t.toUpperCase() : t;
    		// insert arbitrary number of copies of this
    		for (int j = 0; j < r.nextInt(15); j++) {
    			text.append(t);
    		}
    	}
    	
    	System.out.println(text);
    	
    	StringBuilder pattern = new StringBuilder();    
    	int charIndex = 0;
    	while (charIndex < text.length()) {
    		boolean matchSingle = r.nextBoolean();
    		if (matchSingle) {
    			pattern.append('.');
    			charIndex++;
    		} else {
    			char textChar = text.charAt(charIndex);
    			charIndex++;
    			pattern.append(textChar);
    			if (r.nextBoolean()) {
    				pattern.append('*');
    				while (charIndex < text.length() && text.charAt(charIndex) == textChar) {
    					charIndex++;
    					if (r.nextBoolean()) {
    						// arbitrary match some
    						break;
    					}    						
    				}
    			}
    		}

    	}
    	
    	System.out.println(pattern);    	    
    	System.out.println(matchRegex1D(text.toString().toCharArray(),pattern.toString().toCharArray()));
    }

    public static void main(String args[]){
        RegexMatching rm = new RegexMatching();
        rm.generateTestCases();
        
        System.out.println(rm.matchRegex1D("Tushar".toCharArray(),"Tushar".toCharArray()));
        System.out.println(rm.matchRegex1D("Tusha".toCharArray(),"Tushar*a*b*".toCharArray()));
        System.out.println(rm.matchRegex1D("".toCharArray(),"a*b*".toCharArray()));
        System.out.println(rm.matchRegex1D("abbbbccc".toCharArray(),"a*ab*bbbbc*".toCharArray()));
        System.out.println(rm.matchRegex1D("abbbbccc".toCharArray(),"aa*bbb*bbbc*".toCharArray()));
        System.out.println(rm.matchRegex1D("abbbbccc".toCharArray(),".*bcc".toCharArray()));
        System.out.println(rm.matchRegex1D("abbbbccc".toCharArray(),".*bcc*".toCharArray()));
        System.out.println(rm.matchRegex1D("aaa".toCharArray(),"ab*a*c*a".toCharArray()));
        System.out.println(rm.matchRegex1D("aa".toCharArray(), "a*".toCharArray()));
    }
}
