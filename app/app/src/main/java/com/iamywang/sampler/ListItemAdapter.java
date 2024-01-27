// ============================================================================
// This file is part of EavesDroid.
//
// Author: iamywang
// Date Created: Jan 27, 2024
// ============================================================================
package com.iamywang.sampler;

import android.content.Context;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.BaseAdapter;
import android.widget.TextView;

import java.util.LinkedList;

public class ListItemAdapter extends BaseAdapter {
    private final LinkedList<ListItem> mData;
    private final Context mContext;

    public ListItemAdapter(LinkedList<ListItem> mData, Context mContext) {
        this.mData = mData;
        this.mContext = mContext;
    }

    @Override
    public int getCount() {
        return mData.size();
    }

    @Override
    public Object getItem(int position) {
        return null;
    }

    @Override
    public long getItemId(int position) {
        return position;
    }

    @Override
    public View getView(int position, View convertView, ViewGroup parent) {
        convertView = LayoutInflater.from(mContext).inflate(R.layout.item_list, parent, false);

        TextView item_id = convertView.findViewById(R.id.list_number);
        TextView item_title = convertView.findViewById(R.id.list_title);
        TextView item_time = convertView.findViewById(R.id.list_time);

        item_id.setText(String.valueOf(mData.get(position).getId()));
        item_title.setText(mData.get(position).getTitle());
        item_time.setText(mData.get(position).getTime());

        return convertView;
    }
}
