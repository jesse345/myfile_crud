$(document).ready(function(){
    var Profile = {
        Init: function(config) {
            this.config = config;
            this.BindEvents();
        },  
        BindEvents: function() {
            let $this = this.config;

                $this.btn_submit.on('click', {param: 1}, this.Save);
                $this.btn_search.on('click', {param: 1}, this.Search);
                $this.tbl_display.on('click', '.btn-edit', this.Update);
                $this.tbl_display.on('click', '.btn-delete', this.Delete);
                Profile.OnPageLoad();
        },
        OnPageLoad: function(){
            // Profile.Search(1);
        },
        Save: function(e, data){
            var $route  = ( typeof e === 'object' ) ? e.data.param : e,                
                $self = Profile.config;                
                
                switch ($route) {
                    case 1:
                            let $formdata = $self.form_register.serializeArray();
                                // console.log($formdata); return;

                                const $serialize_data = new Common();
                                if($self.btn_submit.attr('data-action') == 'new'){
                                    $method_type = 'POST'
   
                                }
                                if($self.btn_submit.attr('data-action') == 'update'){
                                    $method_type = 'PUT'
                                    $formdata.push({name: 'profile_id', value: $self.btn_submit.attr('data-row-id')});
                                }
                                $payload = { 
                                    url : '/transact/'
                                   ,method_type : $method_type
                                   ,payload : $serialize_data.objectifyForm($formdata)
                                   ,element_id: 'btn-submit'
                               }
                                const $common = new Common($payload);
                                // console.log($payload); return;
                                $common.ApiData()
                                .then(data => {
                                   Profile.Save(2, data)
                                })
                                .catch(err => {
                                    console.log('err',err)
                                })
                    break;
                    case 2:
                            const $result = new Common();
                            
                            if(data.code != 200){
                                alert('error2')
                                return;
                            }
                            let $row = data.data;

                            if( $self.btn_submit.attr('data-action') == 'new' ){

                                let $txt = `
                                    <tr id="${ $row.profile_id }">
                                        <td>${ $row.profile_id }</td>
                                        <td>${ $row.firstname } ${ $row.lastname }</td>
                                        <td>${ $row.address}</td>
                                        <td>${ $row.age}</td>
                                        <td>${ $row.birthday}</td>
                                        <td>
                                            <button class="btn-edit"
                                                data-row-id="${ $row.profile_id }"
                                                data-firstname="${ $row.firstname }"
                                                data-lastname="${ $row.lastname }"
                                                data-address="${ $row.address }"
                                                data-age="${ $row.age }"
                                                data-birthday"${ $row.birthday }"
                                            >Edit</button>
                                            <button
                                                data-row-id="${ $row.profile_id }"
                                            >Delete</button>
                                            
                                        </td>
                                    </tr>
                                    `;
                                
                                $self.tbl_display.append($txt);
                               
                                $self.firstname.val('');
                                $self.lastname.val('');
                                $self.address.val('');
                                $self.age.val('');
                                $self.birthday.val('');

                            }

                            if( $self.btn_submit.attr('data-action') == 'update' ){
                                let $td = $self.tbl_display.find('tr#'+ $row.profile_id).find('td');

                                $td.eq(0).html( $row.profile_name );
                                

                            }
                    break;
                }
        },        
        Update: (e) => {
            let $self = Profile.config;
            let $row_id = e.currentTarget.getAttribute('data-row-id');
            let $name = e.currentTarget.getAttribute('data-name');

            $self.in_name.val($name);
            $self.btn_submit.attr('data-row-id', $row_id);
            $self.btn_submit.attr('data-action', 'update');
            
        },
        Delete: (e) => {
            let $self = Profile.config;
            let $row_id = e.currentTarget.getAttribute('data-row-id');

            
            let $formdata = $self.form_register.serializeArray();

            const $serialize_data = new Common();

            $formdata.push({name: 'profile_id', value: $row_id});
            $payload = { 
                url : '/transact/remove/'
               ,method_type : 'PUT'
               ,payload : $serialize_data.objectifyForm($formdata)
           }
            const $common = new Common($payload);

            $common.ApiData()
            .then(data => {
                if(data.code != 200){
                    alert('error')
                    return;
                }

                $self.tbl_display.find('tr#'+data.profile_id).remove();
            })
            .catch(err => {
                console.log('err',err)
            })
            
        },
        Search: (e, data) => {
            let $route  = (typeof e === 'object') ? e.data.param : e;
            let $self = Profile.config;
            const $result = new Common();

                switch($route){
                    case 1:  
                        
                        let $params = new URLSearchParams();
                        $params.append('name', $self.in_search.val());                          
                        let $url_param = '/transact/?' + $params;    				
                        $payload = {url : $url_param,method_type : 'GET'}
                        const $common = new Common($payload)
                        $common.ApiData()
                        .then(data => {
                            Profile.Search(2,data);
                        })
                        .catch(err => {
                            console.log('err',err)
                        })
                    break;
                    case 2: 
                            if(data.code != 200){
                                alert('error')
                                return;
                            }
                            let $records = data.data, $txt = '';
                            $self.tbl_display.empty(); 
                            $records.forEach($row => {
                                $txt += `
                                    <tr id="${ $row.profile_id }">
                                        <td>${ $row.profile_id }</td>
                                        <td>${ $row.firstname } ${ $row.lastname }</td>
                                        <td>${ $row.address}</td>
                                        <td>${ $row.age}</td>
                                        <td>${ $row.birthday}</td>
                                        <td>
                                            <button class="btn-edit"
                                                data-row-id="${ $row.profile_id }"
                                                data-firstname="${ $row.firstname }"
                                                data-lastname="${ $row.lastname }"
                                                data-address="${ $row.address }"
                                                data-age="${ $row.age }"
                                                data-birthday"${ $row.birthday }"
                                            >Edit</button>
                                            <button class="btn-delete"
                                                data-row-id="${ $row.profile_id }"
                                            >Delete</button>
                                            
                                        </td>
                                    </tr>
                                `;
                            });

                            $self.tbl_display.append($txt); 
                    break;                            
                }
            
        },
        
    }

    Profile.Init({
         form_register : $('#form-register')
        ,firstname : $('#firstname')
        ,lastname : $('#lastname')
        ,address : $('#address')
        ,age : $('#age')
        ,birthday: $('#birthday')
        ,btn_submit : $('#btn-submit')
        ,btn_search : $('#btn-search')
        ,in_search  : $('#in-search')
        ,in_name  : $('#in-name')
        ,tbl_display: $('#tbl-display')

    }) 

})   
