window.addEvent('domready', function() {
    var mousepad = $('mousepad');

    // Setup timer for delaying mouse movement updates.
    var updateMouse = true;
    function updateMouseTimer() { updateMouse = true; }

    // Disable context menu on mousepad.
    mousepad.oncontextmenu = $lambda(false);

    /**
     * Event handlers for relaying updates to server.
     */
    mousepad.addEvent('mousemove', function(e) {
        if (updateMouse == false) return;

        // Calculate position of mouse relative to the pad.
        var pos = this.getPosition();
        var x = e.client.x - pos.x;
        var y = e.client.y - pos.y;

        new Request({
            url: '/mouse/moved',
            data: Hash.toQueryString({x: x, y: y}),
            method: 'post'
        }).send();

        // Start refresh timer to trigger next update.
        // We do this so not to flood the server with updates.
        updateMouse = false;
        updateMouseTimer.delay(500);
    });

    mousepad.addEvent('mousedown', function(e) {
        new Request({
            url: '/mouse/pressed',
            data: Hash.toQueryString({button: e.event.button}),
            method: 'post'
        }).send();
    });

    mousepad.addEvent('mouseup', function(e) {
        new Request({
            url: '/mouse/released',
            data: Hash.toQueryString({button: e.event.button}),
            method: 'post'
        }).send();
    });

    window.addEvent('keydown', function(e) {
        new Request({
            url: '/keyboard/pressed',
            data: Hash.toQueryString({key: e.key, ctrl: e.control, shift: e.shift, alt: e.alt, meta: e.meta}),
            method: 'post'
        }).send();
    });

    window.addEvent('keyup', function(e) {
        new Request({
            url: '/keyboard/released',
            data: Hash.toQueryString({key: e.key, ctrl: e.control, shift: e.shift, alt: e.alt, meta: e.meta}),
            method: 'post'
        }).send();
    });

});
