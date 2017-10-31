
function createOptions(category, description){
    var options = {}
    options.title = {display: true,
                     text: description
    }

    switch (category) {
        case "pie":
            options.cutoutPercentage = 50
            options.animation = {animateScale: true}
            break;
        case "bar":
            options.scales = {yAxes: [{ticks: {beginAtZero:true}}]}
            options.legend = {display: true}
            break;
    }

    return options
}

function createDataSet(category,label,values){
    var dataset = [{
                    label: label,
                    data: values
                }]

    switch (category) {
        case "line":
            dataset[0].backgroundColor = "transparent"
            dataset[0].fill = false
            dataset[0].borderWidth = 2.5
            dataset[0].borderColor = 'rgba(77,166,253,0.85)'
            dataset[0].borderCapStyle = 'butt'
            dataset[0].borderDash = []
            dataset[0].borderJoinStyle = 'miter'
            dataset[0].pointRadius = 1
            dataset[0].pointHitRadius = 10
            dataset[0].pointBackgroundColor = "fff"
            dataset[0].pointBorderWidth = 3
            dataset[0].pointHoverRadius = 5
            dataset[0].pointHoverBorderWidth = 2
            dataset[0].pointHoverBackgroundColor = "rgba(75,192,192,1)"
            dataset[0].pointHoverBorderColor = "rgba(220,220,220,1)"
            dataset[0].pointBorderColor = "rgba(75,192,192,1)"
            break;
        case "pie":
            dataset[0].backgroundColor = ['rgba(255, 51, 51,1)','rgba(153, 255, 51, 1)']
            break;
        case "bar":
            dataset[0].backgroundColor = poolColors(values.length)
            break;
    }

    return dataset
}

function createData(category, keys, values, label){
    return {labels: keys,
        datasets: createDataSet(category,label, values)
    }
}

function createChart(category, context, keys, values, label, description){
    var data = {type: category,
        data: createData(category, keys, values, label),
        options: createOptions(category, description)
    }
    return new Chart(context, data);
}
