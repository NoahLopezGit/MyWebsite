// The typing function
var valid_typing_instance = 0;
const name_bank = [
    "Ronald",
    "Edward",
    "Jason",
    "Jeffrey",
    "Ryan",
    "Jacob",
    "Gary",
    "Nicholas",
    "Eric",
    "Jonathan",
    "Stephen",
    "Larry",
    "Justin",
    "Scott",
    "Brandon",
    "Benjamin",
    "Samuel",
    "Gregory",
    "Alexander",
    "Frank",
    "Patrick",
    "Raymond",
    "Jack",
    "Dennis",
    "Jerry",
    "Tyler",
    "Aaron",
    "Jose",
    "Adam",
    "Nathan",
    "Henry",
    "Douglas",
    "Zachary",
    "Peter",
    "Kyle",
    "Ethan",
    "Walter",
    "Noah",
    "Jeremy",
    "Christian",
    "Keith",
    "Roger",
    "Terry",
    "Gerald",
    "Harold",
    "Sean",
    "Austin",
    "Carl",
    "Arthur",
    "Lawrence",
    "Dylan",
    "Jesse",
    "Jordan",
    "Bryan",
    "Billy",
    "Joe",
    "Bruce",
    "Gabriel",
    "Logan",
    "Albert",
    "Willie",
    "Alan",
    "Juan",
    "Wayne",
    "Elijah",
    "Randy",
    "Roy",
    "Vincent",
    "Ralph",
    "Eugene",
    "Russell",
    "Bobby",
    "Mason",
    "Philip",
    "Louis",
    "Patricia",
    "Jennifer",
    "Linda",
    "Elizabeth",
    "Barbara",
    "Susan",
    "Jessica",
    "Sarah",
    "Karen",
    "Lisa",
    "Nancy",
    "Betty",
    "Margaret",
    "Sandra",
    "Ashley",
    "Kimberly",
    "Emily",
    "Donna",
    "Michelle",
    "Carol",
    "Amanda",
    "Dorothy",
    "Melissa",
    "Deborah",
    "Stephanie",
    "Rebecca",
    "Sharon",
    "Laura",
    "Cynthia",
    "Kathleen",
    "Amy",
    "Angela",
    "Shirley",
    "Anna",
    "Brenda",
    "Pamela",
    "Emma",
    "Nicole",
    "Helen",
    "Samantha",
    "Katherine",
    "Christine",
    "Debra",
    "Rachel",
    "Carolyn",
    "Janet",
    "Catherine",
    "Maria",
    "Heather",
    "Diane",
    "Ruth",
    "Julie",
    "Olivia",
    "Joyce",
    "Virginia",
    "Victoria",
    "Kelly",
    "Lauren",
    "Christina",
    "Joan",
    "Evelyn",
    "Judith",
    "Megan",
    "Andrea",
    "Cheryl",
    "Hannah",
    "Jacqueline",
    "Martha",
    "Gloria",
    "Teresa",
    "Ann",
    "Sara",
    "Madison",
    "Frances",
    "Kathryn",
    "Janice",
    "Jean",
    "Abigail",
    "Alice",
    "Julia",
    "Judy",
    "Sophia",
    "Grace",
    "Denise",
    "Amber",
    "Doris",
    "Marilyn",
    "Danielle",
    "Beverly",
    "Isabella",
    "Theresa",
    "Diana",
    "Natalie",
    "Brittany",
    "Charlotte",
    "Marie",
    "Kayla",
    "Alexis",
    "Lori"
];

async function typeText(text) {
    var heading = document.getElementById("welcome_tag");
    var personal_typing_instance = valid_typing_instance + 1;
    valid_typing_instance = personal_typing_instance;
    var max = name_bank.length;
    var text = name_bank[Math.floor(Math.random() * max)]; //eventually I want to request this from my server... for now it has the ghetto solution
    var word = "";
    var j = 0;
    var word_interval = setInterval(typechar,150)
    var msg1 = "Welcome ";
    var msg2 = ", we've been waiting";

    function typechar(){
        if (j < text.length && personal_typing_instance == valid_typing_instance){
            word += text.charAt(j)
            heading.innerHTML = msg1 + word + msg2;
        } else if (j >= text.length && personal_typing_instance == valid_typing_instance) {
            if (j%8==0){
                heading.innerHTML = msg1 + word + "|" + msg2; 
            } else if (j % 8 == 4){
                typing_char = " "
                heading.innerHTML = msg1 + word + " " + msg2;
            }
        } else if (personal_typing_instance!=valid_typing_instance) {
            clearInterval(word_interval);
        }
        j++;
    }
}

function changing_welcome_message(){
    var i = 0;
    typeText("test")
    function myloop() {
        setTimeout(function() {
            typeText("test");
            i++;
            if (i < 20) {
                myloop();
            }
        }, 10000)
        }
        myloop();
}
