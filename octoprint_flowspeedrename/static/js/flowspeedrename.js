/*
 * View model for OctoPrint-Flowspeedrename
 *
 * Author: ntoff
 * License: AGPLv3
 */
$(function() {
    function FlowspeedrenameViewModel(parameters) {
        var self = this;
        self.settings = parameters[0];

        self.settings.feedname = new ko.observable(null);
        self.settings.flowname = new ko.observable(null);

        self.onBeforeBinding = function () {
            self.settings.feedname(self.settings.settings.plugins.flowspeedrename.feedname());
            self.settings.flowname(self.settings.settings.plugins.flowspeedrename.flowname());
            try {
                $(".jog-panel").find("button:contains('Feed')").eq(0).html("" + self.settings.feedname() + ":<span data-bind=\"text: feedRate() + '%'\"></span>");
                $("#control-jog-extrusion").find("button:contains('Flow')").eq(0).html("" + self.settings.flowname() + ":<span data-bind=\"text: flowRate() + '%'\"></span>");
            }
            catch (error) {
                console.log(error);
            }
        }


            
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: FlowspeedrenameViewModel,
        dependencies: ["settingsViewModel"],
        elements: [  ]
    });
});
