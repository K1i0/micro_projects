(async() => {
    let data = {
       "total":100,
       "lastPage":false,
       "items": [] //Заменить [] данными из result.json
    }
    
    let items = data.items;
    let dictionaryId = "c0f7b305-7310-4cff-8da8-5a3c49dbf9a5" // Тут id спавочника
    for (let i = 0; i < items.length; i++) {
       if (i % 10 == 0) {
          console.log("Готово на " + (i / items.length) * 100 + "%");
       }
       let item = items[i];
       await $.ajax({
          type: "POST",
          url: "/rest/dictionary/" + dictionaryId + "/item",
          contentType: "application/json",
          data: JSON.stringify({"code":item.code,"name":item.fullname})
      });
    }
 })()