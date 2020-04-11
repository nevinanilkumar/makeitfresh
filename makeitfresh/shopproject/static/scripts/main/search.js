search = function() {
    const search_box = document.querySelector("#search_box");
    const card_deck = document.querySelector("#card_deck");
    const CARD_DECK_HTML = card_deck.innerHTML;
    
    function create_card_deck() {
        return `<div class="card-deck mt-4 mb-2" id = "card_deck"></div>`;
    }

    function create_card(shopname, phonenumber) {
        return `
        <div class="card">
        <img class="card-img-top" src="../../static/icons/iconshop.jpg" alt="Card image cap">
        <div class="card-body">
          <h5 class="card-title">${shopname}</h5>
          <p class="card-text">
              Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
              Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.</p>
        </div>
        <div class="card-footer">
          <small class="text-muted">Shop Closed|opens 3 PM</small><br/>
          <small class="text-muted">Phone: ${phonenumber}</small>
        </div>
        `;
    }
    function create_request(url, name, load_event) {
        req = new XMLHttpRequest();
        req.open("GET", url+name);
        req.responseType = "json";
        req.onload = load_event;
        console.log(req);
        return req
    }

    search_box.addEventListener("keyup", searchEvent);
    function searchEvent(event) {
        if (event.target.value !== "") {
            url = "http://127.0.0.1:5000/?shop="+event.target.value;
            request = new XMLHttpRequest();
            request.open("GET", url);
            request.responseType = "json";
            request.onload = function(e) {
                if (request.status == 200) {
                    console.log(request.response);
                    obj = request.response[0];
                    card_deck.innerHTML = create_card(obj.name, obj.phone_number);
                }
            }
            
            request.send();
            console.log(request);
        }
        else {
            card_deck.innerHTML = CARD_DECK_HTML;
            console.log("no input");
        }
    }

}()