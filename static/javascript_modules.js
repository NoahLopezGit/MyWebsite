// The typing function
let valid_typing_instance = 0;
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

function typeText() {
    let heading = document.getElementById("welcome_tag");
    let personal_typing_instance = valid_typing_instance + 1;
    valid_typing_instance = personal_typing_instance;
    let max = name_bank.length;
    let text = name_bank[Math.floor(Math.random() * max)]; //eventually I want to request this from my server... for now it has the ghetto solution
    let word = "";
    let j = 0;
    let word_interval = setInterval(typechar,150)
    let msg1 = "Welcome ";
    let msg2 = ", we've been waiting";

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
    let i = 0;
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

function type_response(message) {
    console.log('test')
    let word = "";
    let j = 0;
    let word_interval = setInterval(typechar, 75)
    let heading = document.getElementById('console_history');
    heading.innerHTML += "<p></p";
    response_line = heading.children[heading.children.length-1];
    function typechar() {
        if (j < message.length) {
            word += message.charAt(j);
            response_line.innerHTML = word;
        } else {
            console.log('test');
            clearInterval(word_interval);
            // heading.innerHTML += "<p class='parent'>>"+
            //     "<input autocomplete='off' id='user_input' type='text' name='user_input' class='rq-form-element' autofocus/></p>";
            enter_event_listener();
        }
        j++;
    }
}

function enter_event_listener(){
    // Get the input field
    let console_history = document.getElementById('console_history');
    let input_div = document.getElementById('user_input');
    input_div.innerHTML = "<p class='parent'>>" +
        "<input class='child' name='user_input' autocomplete='off' type='text' autofocus/>" +
        "</p>";
    let input_parent = input_div.children[0];

    // Execute a function when the user presses a key on the keyboard
    input_parent.addEventListener("keypress", function (event) {
        // If the user presses the "Enter" key on the keyboard
        if (event.key === "Enter") {
            // //fetch with input.value
            let user_input = input_parent.children[0].value;
            console_history.innerHTML += "<div class='parent'>><p class='child'>" + 
                user_input+"</p></div>";
            input_parent.remove();
            fetch('/API/talk_to_me/' + user_input)
            .then((server_response) => server_response.json())
            .then((return_val) => return_val.response)
            .then((return_val) => type_response(return_val));
        }
    });
}    

function get_mc_server_status(){
    let server_status_element = document.getElementById('mc_server_status')
    fetch('/API/minecraft')
        .then((server_response) => server_response.json())
        .then((return_val) => return_val.mc_server_status)
        .then((mc_server_status) => server_status_element.innerHTML=mc_server_status)
}