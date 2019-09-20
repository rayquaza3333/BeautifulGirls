var GMapHandler = new Class({
    Implements: Options,
    options: {
        addMarkerToCentre: true,
        center: '',
        latitude: 'lon',
        longitude: 'lat',
        controls: false,
        oMap: 'gmap',
        zoom: 14
    },
    map: false,
    initialize: function(gmap, options) {
        var self = this;
        options.oMap = gmap;
        this.setOptions(options);
        latitude = this.options.latitude.toFloat();
        longitude = this.options.longitude.toFloat();
        myLatlng = new google.maps.LatLng(latitude, longitude);
        var myOptions = {
            zoom: this.options.zoom.toInt(),
            center: myLatlng,
            mapTypeControl: this.options.controls,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        }
        var points = this.options.oMap.getElements('span.marker');
        this.map = new google.maps.Map((this.options.oMap), myOptions);
        if (points.length) {
            points.each(function(point) {
                var options = JSON.decode(point.getAttribute('rel'));
                loc = new google.maps.LatLng(options.latitude, options.longitude);
                var info = point.get('html');
                if (options.marker !== false) {
                    var marker = new google.maps.Marker({
                        position: loc,
                        map: self.map
                    })
                    if (info.length) {
                        var popup = new google.maps.InfoWindow({
                            content: info
                        })
                        google.maps.event.addListener(marker, 'click', function() {
                            popup.open(self.map, marker);
                        });
                    }
                }
            });
        }
        gmap.store('gmap', this);
    },
    setCenter: function(lat, lon, zoom) {
        this.map.setCenter(new google.maps.LatLng(lat, lon));
        this.map.setZoom(zoom);
    }
});
var HomeShow = new Class({
    Implements: Options,
    options: {
        'container': 'homeshow',
        'controlsCurrentClass': 'current',
        'duration': 7000,
        'slides': 'div.slide',
        'transition': 700
    },
    initialize: function(options) {
        this.setOptions(options);
        this.container = $(this.options.container);
        this.slides = this.container.getElements(this.options.slides);
        this.slideHeight = this.slides[0].getStyle('height');
        this.slides.setStyles({
            'left': 0,
            'position': 'absolute',
            'top': this.slideHeight
        }).set('tween', {
            'duration': this.options.transition,
            'transition': 'sine:in:out'
        });
        this.slides[0].setStyle('top', 0);
        this.currentSlide = 0;
        this.nextSlide = 1;
        this.buildControls();
        this.run();
    },
    advance: function() {
        var self = this;
        this.slides[this.nextSlide].setStyle('top', this.slideHeight);
        this.slides[this.currentSlide].tween('top', '-' + self.slideHeight + 'px');
        this.controls.getElements('li.' + this.options.controlsCurrentClass).removeClass(this.options.controlsCurrentClass);
        var nextSlide = this.nextSlide + 1;
        if (nextSlide >= this.slides.length) nextSlide = 0;
        this.controls.getElement('li:nth-child(' + (this.nextSlide + 1) + ')').addClass(self.options.controlsCurrentClass);
        this.slides[this.nextSlide].tween('top', 0).get('tween').chain(function() {
            self.slides[self.currentSlide].setStyle('top', self.slideHeight);
            self.currentSlide = self.nextSlide;
            self.nextSlide = nextSlide;
        });
    },
    advanceTo: function(slideNo) {
        $clear(this.periodical);
        this.nextSlide = slideNo;
        this.advance();
        this.run();
    },
    buildControls: function() {
        var self = this;
        this.controls = new Element('ol', {
            'class': 'controls'
        }).inject(self.container);
        for (var i = 1; i <= this.slides.length; i++) {
            this.controls.adopt(new Element('li', {
                'class': (i == 1) ? 'current' : '',
                'events': {
                    'click': function() {
                        if (this.get('text') - 1 != self.currentSlide) self.advanceTo(this.get('text') - 1);
                        this.addClass(self.options.controlsCurrentClass);
                    }
                },
                'text': i
            }));
        }
    },
    run: function() {
        this.periodical = (function() {
            this.advance();
        }).periodical(this.options.duration, this);
    }
});
var Quiz = new Class({
    blockNo: 1,
    responses: [{
        upperBound: "30",
        name: "Beginner/Elementary - A1/A2",
        response: "Bạn có thể hiểu được một vài từ tiếng anh, có thể tương tác với những người khác một cách đơn giản miễn là người kia nói chậm, rõ ràng và sẵn sàng giúp đỡ."
    }, {
        upperBound: "50",
        name: "Pre-Intermediate - Tiền trung cấp",
        response: "Bạn có kiến thức ngữ pháp cơ bản, bạn có thể giao tiếp một cách tương đối và trao đổi thông tin về những vấn đề quen thuộc thường gặp trong công việc, học tập, giải trí"
    }, {
        upperBound: "68",
        name: "Intermediate - B1",
        response: "Có thể hiểu được ý chính của những văn bản phức tạp về các chủ đề cụ thể và trừu tượng, giao tiếp ở mức độ lưu loát và khá tự nhiên, bao gồm cả các thảo luận kỹ thuật về lĩnh vực chuyên môn của mình"
    }, {
        upperBound: "88",
        name: "Upper Intermediate - B2",
        response: "Bạn có thể nắm được ý chính của văn bản phức tạp, ngôn ngữ nói tiêu chuẩn, phát trực tiếp hoặc phát sóng truyền hình, giao tiếp với các nội dung có từ vựng đọc rộng, thể hiện ý kiến tự do"
    }, {
        upperBound: "100",
        name: "Advanced - C1",
        response: "Bạn có thể hiểu được nhiều loại văn bản dài, khó hiểu và nhận ra ý nghĩa tiềm ẩn, diễn đạt các ý tưởng một cách trôi chảy và tự nhiên một cách linh hoạt và hiệu quả cho các mục đích xã hội, học thuật và công việc. Có thể viết các văn bản rõ ràng, chi tiết và có cấu trúc tốt về các chủ đề phức tạp, làm chủ việc sử dụng các mô hình tổ chức, từ nối và phương tiện liên kết."
    }],
    initialize: function() {
        var self = this;
        $$('ul.answers li').addEvents({
            'click': function() {
                this.getParent().getPrevious('p').getElement('span.answer').set('text', this.get('text'));
                this.addClass('selected').getSiblings().removeClass('selected');
            },
            'mouseenter': function() {
                this.addClass('hover');
            },
            'mouseleave': function() {
                this.removeClass('hover');
            }
        });
        $$('#quiz a.finish').addEvent('click', function(e) {
            e.stop();
            self.finish();
        });
        $$('#quiz a.next_block').addEvent('click', function(e) {
            e.stop();
            self.blockMove(1);
        });
        $$('#quiz a.previous_block').addEvent('click', function(e) {
            e.stop();
            self.blockMove(-1);
        });
        $('quiz_progress').getElement('li:first-child').addClass('completed').set('html', '&raquo;');
    },
    blockMove: function(increment) {
        var self = this;
        $('block_' + this.blockNo).setStyle('display', 'none');
        this.blockNo += increment;
        $('block_' + this.blockNo).setStyle('display', 'block');
        $('quiz_progress').getElements('li').each(function(li, i) {
            if (i < self.blockNo) li.addClass('completed').set('html', '&raquo;');
            else li.removeClass('completed');
        });
        new Fx.Scroll(window).toElement('quiz_progress');
    },
    finish: function() {
        new Fx.Scroll(window).toElement('quiz_progress');
        var total = 0;
        $$('ul.answers li.selected').each(function(li) {
            if (li.get('rel') == 'correct') total = total + 5;
        });
        $$('ul.answers li[rel="correct"]').addClass('correct');
        $('block_final').getElement('div.number').set('text', total + '%');
        sessionStorage.diemhocvien = total;
        var level = "";
        var message = "";
        this.responses.each(function(response) {
            if (total <= response.upperBound && level == "") {
                level = response.name;
                message = response.response;
            }
        });
        level = "Level " + level + ".";
        $('block_final').getElement('h2.level').set('text', level);
        $('block_final').getElement('p.descriptor').set('text', message);
        $$('#quiz a').setStyle('display', 'none');
        $$('div.question_block').setStyle('display', 'block');
    }
});
var Shared = new Class({
    initialize: function() {
        this.initNav();
        if ($('homeshow')) new HomeShow();
        if ($('subnav')) {
            $$('li.expander, li.expanded').each(function(li) {
                var subcat = li.getElement('ul');
                if (subcat) {
                    subcat.setStyle('display', 'block');
                    var subcatSlide = new Fx.Slide(subcat, {
                        'duration': 'short'
                    });
                    if (li.hasClass('expander')) subcatSlide.hide();
                    li.addEvent('click', function(e) {
                        if (e) e.stopPropagation();
                        subcatSlide.toggle();
                        if (li.hasClass('expander')) li.removeClass('expander').addClass('expanded');
                        else li.removeClass('expanded').addClass('expander');
                    });
                    li.getElement('a').addEvent('click', function(e) {
                        var event = new Event(e).stop();
                        if (!subcatSlide.open) {
                            $(event.target).getParent().fireEvent('click');
                        } else {
                            document.location.href = this.get('href');
                        }
                    });
                }
            });
            $('subnav').getElements('a').each(function(link) {
                link.addEvent('click', function(e) {
                    e.stopPropagation();
                });
            });
        }
        var coursesFeatures = $$('div.course, div.feature');
        coursesFeatures.addEvents({
            'click': function() {
                if (link = this.getElement('h2 a')) {
                    document.location.href = link.get('href');
                }
            },
            'mouseenter': function() {
                if (link = this.getElement('h2 a')) {
                    this.addClass('hover');
                }
            },
            'mouseleave': function() {
                this.removeClass('hover');
            }
        });
        coursesFeatures.each(function(div) {
            new Element('span', {
                'class': 'more',
                'html': '&nbsp;'
            }).inject(div);
        });
        $$('div.gallery a').each(function(element) {
            new ReMooz(element, {
                centered: true,
                origin: element.getElement('img')
            });
        });
        var gmaps = $$('div.gmap');
        if (gmaps.length) {
            gmaps.each(function(gmap) {
                var options = gmap.getAttribute('rel');
                options = JSON.decode(options);
                new GMapHandler(gmap, options);
            });
        }
        if ($('quiz')) new Quiz();
        if ($('promo_video')) this.initVideo();
        if (document.location.pathname == '/courses/teacher-training/cambridge-celta') {
            var docLinks = $$('a[href$=".docx"]');
            if (docLinks.length) {
                var forms = $$('form[action="/forms/application"]');
                forms.addEvent('submit', function(e) {
                    e.stop();
                    document.location.href = docLinks[0].get('href');
                    var SM = new SimpleModal({
                        "hideFooter": true,
                        "width": 580
                    });
                    SM.show({
                        "title": 'CELTA Application Form',
                        "model": "modal",
                        "contents": "<p>Your Cambridge CELTA application form has been downloaded - you should check your computer's Downloads folder for the file."
                    });
                });
            }
        }
    },
    initNav: function() {
        var nav = $('header').getElement('div.nav');
        var navCoords = nav.getCoordinates();
        $('header').getElement('div.nav ul').getElements('ul').each(function(ul) {
            var parentUls = ul.getParents('ul').length;
            var ulCoords = ul.getCoordinates($('header').getElement('.nav'));
            if (ulCoords.left + ulCoords.width > 940) {
                var parentUls = ul.getParents('ul');
                if (parentUls.length == 1) {
                    ul.setStyle('left', -(ulCoords.left + ulCoords.width - 940));
                } else if (parentUls.length < 3) {
                    ul.setStyle('left', -ulCoords.width);
                    ul.getElements('ul').setStyle('left', -ulCoords.width);
                }
            }
        });
        $$('#header div.nav > ul > li > ul').each(function(ul) {
            var ulOffset = isNaN(ul.getStyle('left').toInt()) ? 0 : Math.abs(ul.getStyle('left').toInt());
            var topLink = ul.getPrevious('a');
            new Element('li', {
                'class': 'heading',
                'html': topLink.get('html')
            }).adopt(new Element('span', {
                'class': 'arrow',
                'html': '&nbsp;',
                'styles': {
                    'left': ((topLink.getSize().x - 10) / 2) + ulOffset
                }
            })).inject(ul, 'top');
        });
    },
    initVideo: function() {
        $('promo_video').addEvent("click", function(e) {
            e.stop();
            var SM = new SimpleModal({
                "hideFooter": true,
                "width": 580
            });
            SM.show({
                "title": 'ILS English',
                "model": "modal",
                "contents": '<iframe width="560" height="315" src="http://www.youtube.com/embed/D36eWyOrfx8?autoplay=1" frameborder="0" allowfullscreen></iframe>'
            });
        });
    }
});
var SimpleModal = new Class({
    Implements: [Options],
    request: null,
    buttons: [],
    options: {
        onAppend: Function,
        offsetTop: null,
        overlayOpacity: .4,
        overlayColor: "#000000",
        overlayDuration: 100,
        width: 400,
        draggable: true,
        keyEsc: true,
        overlayClick: true,
        closeButton: true,
        hideHeader: false,
        hideFooter: false,
        btn_ok: "OK",
        btn_cancel: "Cancel",
        template: "<div class=\"simple-modal-header\"> \
            <h1>{_TITLE_}</h1> \
          </div> \
          <div class=\"simple-modal-body\"> \
            <div class=\"contents\">{_CONTENTS_}</div> \
          </div> \
          <div class=\"simple-modal-footer\"></div>"
    },
    initialize: function(options) {
        this.setOptions(options);
    },
    show: function(options) {
        if (!options) options = {};
        this._overlay("show");
        switch (options.model) {
            case "confirm":
                this.addButton(this.options.btn_ok, "btn primary btn-margin", function() {
                    try {
                        options.callback()
                    } catch (err) {};
                    this.hide();
                })
                this.addButton(this.options.btn_cancel, "btn secondary");
                var node = this._drawWindow(options);
                this._addEscBehaviour();
                break;
            case "modal":
                var node = this._drawWindow(options);
                this._addEscBehaviour();
                break;
            case "modal-ajax":
                var node = this._drawWindow(options);
                this._loadContents({
                    "url": options.param.url || "",
                    "onRequestComplete": options.param.onRequestComplete || Function
                })
                break;
            default:
                this.addButton(this.options.btn_ok, "btn primary");
                var node = this._drawWindow(options);
                this._addEscBehaviour();
                break;
        }
        node.setStyles({
            width: this.options.width
        });
        if (this.options.hideHeader) node.addClass("hide-header");
        if (this.options.hideFooter) node.addClass("hide-footer");
        if (this.options.closeButton) this._addCloseButton();
        if (this.options.draggable) {
            var headDrag = node.getElement(".simple-modal-header");
            new Drag(node, {
                handle: headDrag
            });
            headDrag.setStyle("cursor", "move")
            node.addClass("draggable");
        }
        this._display();
    },
    hide: function() {
        try {
            if (typeof(this.request) == "object") this.request.cancel();
        } catch (err) {}
        this._overlay('hide');
        return;
    },
    _drawWindow: function(options) {
        var node = new Element("div#simple-modal", {
            "class": "simple-modal"
        });
        node.inject($$("body")[0]);
        var html = this._template(this.options.template, {
            "_TITLE_": options.title || "Untitled",
            "_CONTENTS_": options.contents || ""
        });
        node.fade('hide');
        node.set("html", html);
        node.set('tween', this.options.overlayDuration);
        node.fade('in');
        this._injectAllButtons();
        this.options.onAppend();
        return node;
    },
    addButton: function(label, classe, clickEvent) {
        var bt = new Element('a', {
            "title": label,
            "text": label,
            "class": classe,
            "events": {
                click: (clickEvent || this.hide).bind(this)
            }
        });
        this.buttons.push(bt);
        return bt;
    },
    _injectAllButtons: function() {
        this.buttons.each(function(e, i) {
            e.inject($("simple-modal").getElement(".simple-modal-footer"));
        });
        return;
    },
    _addCloseButton: function() {
        var b = new Element("a", {
            "class": "close",
            "href": "#",
            "html": "x"
        });
        b.inject($("simple-modal"), "top");
        b.addEvent("click", function(e) {
            if (e) e.stop();
            this.hide();
        }.bind(this))
        return b;
    },
    _overlay: function(status) {
        switch (status) {
            case 'show':
                this._overlay('hide');
                var overlay = new Element("div", {
                    "id": "simple-modal-overlay"
                });
                overlay.inject($$("body")[0]);
                overlay.setStyle("background-color", this.options.overlayColor);
                overlay.set('tween', {
                    duration: this.options.overlayDuration
                });
                overlay.fade("hide").fade(this.options.overlayOpacity);
                if (this.options.overlayClick) {
                    overlay.addEvent("click", function(e) {
                        if (e) e.stop();
                        this.hide();
                    }.bind(this))
                }
                this.__resize = this._display.bind(this);
                window.addEvent("resize", this.__resize);
                break;
            case 'hide':
                window.removeEvent("resize", this._display);
                if (this.options.keyEsc) {
                    var fixEV = Browser.name != 'ie' ? "keydown" : "onkeydown";
                    window.removeEvent(fixEV, this._removeSM);
                }
                try {
                    $('simple-modal-overlay').destroy();
                } catch (err) {}
                try {
                    $('simple-modal').destroy();
                } catch (err) {}
                break;
        }
        return;
    },
    _loadContents: function(param) {
        $('simple-modal').addClass("loading");
        var re = new RegExp(/([^\/\\]+)\.(jpg|png|gif)$/i);
        if (param.url.match(re)) {
            $('simple-modal').addClass("hide-footer");
            $("simple-modal-overlay").removeEvents();
            var images = [param.url];
            new Asset.images(images, {
                onProgress: function(i) {
                    immagine = this;
                },
                onComplete: function() {
                    try {
                        $('simple-modal').removeClass("loading");
                        var content = $('simple-modal').getElement(".contents");
                        var padding = content.getStyle("padding").split(" ");
                        var width = (immagine.get("width").toInt()) + (padding[1].toInt() + padding[3].toInt())
                        var height = immagine.get("height").toInt();
                        var myFx1 = new Fx.Tween($("simple-modal"), {
                            duration: 'normal',
                            transition: 'sine:out',
                            link: 'cancel',
                            property: 'width'
                        }).start($("simple-modal").getCoordinates().width, width);
                        var myFx2 = new Fx.Tween(content, {
                            duration: 'normal',
                            transition: 'sine:out',
                            link: 'cancel',
                            property: 'height'
                        }).start(content.getCoordinates().height, height).chain(function() {
                            immagine.inject($('simple-modal').getElement(".contents").empty()).fade("hide").fade("in");
                            this._display();
                            this._addEscBehaviour();
                        }.bind(this));
                        var myFx3 = new Fx.Tween($("simple-modal"), {
                            duration: 'normal',
                            transition: 'sine:out',
                            link: 'cancel',
                            property: 'left'
                        }).start($("simple-modal").getCoordinates().left, (window.getCoordinates().width - width) / 2);
                    } catch (err) {}
                }.bind(this)
            });
        } else {
            this.request = new Request.HTML({
                evalScripts: false,
                url: param.url,
                method: 'get',
                onRequest: function() {},
                onSuccess: function(responseTree, responseElements, responseHTML, responseJavaScript) {
                    $('simple-modal').removeClass("loading");
                    $('simple-modal').getElement(".contents").set("html", responseHTML);
                    param.onRequestComplete();
                    eval(responseJavaScript)
                    this._display();
                    this._addEscBehaviour();
                }.bind(this),
                onFailure: function() {
                    $('simple-modal').removeClass("loading");
                    $('simple-modal').getElement(".contents").set("html", "loading failed")
                }
            }).send();
        }
    },
    _display: function() {
        try {
            $("simple-modal-overlay").setStyles({
                height: window.getCoordinates().height
            });
        } catch (err) {}
        try {
            $("simple-modal").setStyles({
                top: ((window.getCoordinates().height - $("simple-modal").getCoordinates().height) / 2 - 100),
                left: ((window.getCoordinates().width - $("simple-modal").getCoordinates().width) / 2)
            });
        } catch (err) {}
        return;
    },
    _addEscBehaviour: function() {
        if (this.options.keyEsc) {
            this._removeSM = function(e) {
                if (e.key == "esc") this.hide();
            }.bind(this)
            if (this.options.keyEsc) {
                var fixEV = Browser.name != 'ie' ? "keydown" : "onkeydown";
                window.addEvent(fixEV, this._removeSM);
            }
        }
    },
    _template: function(s, d) {
        for (var p in d)
            s = s.replace(new RegExp('{' + p + '}', 'g'), d[p]);
        return s;
    }
});
var shared = null;
window.addEvent('domready', function() {
    shared = new Shared();
});