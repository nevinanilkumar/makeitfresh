let namespace = function () {
  const SEARCH = document.querySelector("#search_box");
  const CARD = document.querySelector(".card");
  const CARDS = document.querySelector("#cards").cloneNode(deep = true);
  const DECKSIZE = 3;
  SEARCH.addEventListener("keyup", searchEvent);


  function create_card(name="", num="", display="hidden") {
    const card = CARD.cloneNode(deep = true);
    const title = card.querySelector(".card-title");
    const phone_number = card.querySelectorAll(".text-muted")[1];
    title.textContent = name;
    phone_number.textContent = num;
    card.style.visibility=display;
    return card;
  }


  function create_deck() {
    const deck = document.createElement("div");
    deck.className = "card-deck mb-4";
    return deck;
  }


  function searchEvent(event) {
    const cards = document.querySelector("#cards");
    const new_cards = document.createElement("div");
    if (event.target.value !== ""){
      const obj = get_obj(`shop=${event.target.value}`);
      obj.onload = function(e) {
        if (obj.response.length > 0) {
          let deck;
          obj.response.forEach(
            (shop,index) => {
              if(index % DECKSIZE === 0) {
                console.log(index);
                deck = create_deck();
                new_cards.appendChild(deck);
                
              }
              deck.appendChild(create_card(shop.name,shop.phone_number, "visible"));
            });
            if (obj.response.length % DECKSIZE !== 0 && (window.innerWidth > 575)) {
              for(let i = 0, len=obj.response.length; i < DECKSIZE - len % DECKSIZE; i++) 
                deck.append(create_card());
                
            }
          new_cards.appendChild(deck);
        }
        cards.innerHTML = new_cards.innerHTML;
      }
    }
    else {
      cards.innerHTML = CARDS.innerHTML;
    }
  }


  function get_obj(txt) {
    url = "http://127.0.0.1:5000/?"
    req = new XMLHttpRequest();
    req.open("GET", url + txt, true);
    req.responseType = "json";
    req.send()
    return req;
  }

}()
