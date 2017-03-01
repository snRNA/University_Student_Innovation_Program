<?php

namespace App\Http\Controllers;

use DB;
use Illuminate\Http\Response as HttpResponse;
use Illuminate\Http\Request;

use App\Http\Requests;
use App\Http\Controllers\Controller;

class StatusController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
    }

    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        //
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
    }

    public function storestatus(Request $request)
    {
        $input = $request->all();
        $name = $input['name'];
        $value = $input['value'];
        $timestamp = $input['timestamp'];
        $readtime = $input['read_time'];
        $status = array('name'=>$name,'value'=>$value,'timestamp'=>$timestamp,'readtime'=>$readtime);
        $res = DB::select('select * from status where name = ?',[$name]);
        if(!empty($res)) {
            $res = DB::table('status')->update(['value' => $value, 'timestamp' => $timestamp, 'readtime' => $readtime]);
            return 'success';
        }
        else
        {
            $res = DB::table('status')->insert($status);
            return 'success';
        }
    }

    public function getstatus()
    {
        $data = DB::select('select * from status');

        return view('test',['data'=>$data]);
    }

}
